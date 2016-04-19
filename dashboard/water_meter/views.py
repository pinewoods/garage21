import datetime
import calendar
import collections
from bisect import bisect_left

import pytz

from django.db.models.query import QuerySet
from django.db.models import Max
from django.http import Http404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions

from pinewoods_timeseries.views import GenericViewCurrentReading

from .models import YFS201Reading
from .models import HCSR04Reading
from .models import HCSR04ReadingSerializer
from .models import YFS201ReadingSerializer
from .models import EssentialHCSR04Serializer
from .models import WaterTank
from .models import ConsumpitionGoal
from .models import ConsumpitionGoalSerializer
from .models import GoalSerializer

from .querysets import MonthBoundary

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('post',))
def root_endpoint(request, format=None):

    try:
        wt = WaterTank.objects.get(pk=1)

        level_reading = HCSR04Reading(
                sensor_reading=request.data['echo'],
                water_tank=wt)

        flow_reading = YFS201Reading(
                sensor_reading=request.data['total_liters'],
                water_tank=wt)

        level_reading.save()
        flow_reading.save()
    except:
        pass
        from IPython import embed; embed()

    return Response(status=status.HTTP_204_NO_CONTENT)

"""
class ViewReadings(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        " ""
        Recives data from sensors.
        " ""
        try:
            wt = WaterTank.objects.get(pk=1)

            level_reading = HCSR04Reading(
                    sensor_reading=request.data['echo'],
                    water_tank=wt)

            flow_reading = YFS201Reading(
                    sensor_reading=request.data['total_liters'],
                    water_tank=wt)

            level_reading.save()
            flow_reading.save()
        except:
            #pass
            from IPython import embed; embed()

        return Response(status=status.HTTP_204_NO_CONTENT)
"""

class ViewCurrentTankLevel(GenericViewCurrentReading):
    lookup_field = 'water_tank'
    serializer_class = HCSR04ReadingSerializer
    model_class = HCSR04Reading


class ViewIntradayTankLevel(ListAPIView):
    lookup_field = 'water_tank'
    serializer_class = EssentialHCSR04Serializer
    queryset = HCSR04Reading.timeseries.day(
            datetime.date.today()).order_by('-timestamp')


class ViewMonthlyGoals(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, water_tank, year, month):
        """
            Return data for the monthly goals burndown chart.
        """
        year, month = int(year), int(month)
        mb = MonthBoundary(year, month)
        days_count = mb.last.day

        # TODO: recover YFS201Reading using Sabesp's RGI
        wt = WaterTank.objects.get(pk=water_tank)
        user = wt.user

        # TODO: Factor out
        from sabesp.models import SabespProfile
        sabesp_goal = SabespProfile.objects.get(
                user=user).consumption_goal

        # TODO: Match Goal's month
        pinewoods_goal = ConsumpitionGoal.objects.latest(
                'goal_initial').goal

        readings = list(YFS201Reading.timeseries.filter(
                water_tank=wt).month(datetime.date(year,month, 1)
                        ).daily_closing)

        # 1m^3 = 1000 liters
        consumption = [(c.read() - readings[0].read()) / 1000.
                for c in readings]

        response = {
                "sabesp_goal": sabesp_goal,
                "sabesp_step": sabesp_goal / days_count,
                "pinewoods_goal": pinewoods_goal,
                "pinewoods_step": pinewoods_goal / days_count,
                "days_count": days_count,
                "consumption": consumption,
         }

        return Response(response)


class ViewMonthlyReadings(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, year):
        user = self.request.user
        wt = WaterTank.objects.filter(user=user)
        year = datetime.date(int(year), 1, 1)

        sensor_reading= YFS201Reading.timeseries.filter(
            water_tank=wt).year(year).monthly_closing

        # 1m^3 = 1000 liters
        month_dict = {r.timestamp.month: r.read() / 1000.
                for r in sensor_reading}

        response = {
            "sensor_reading": [month_dict.get(m, None)
                for m in range(1, 13)],
        }

        return Response(response)


class GoalsViewSet(viewsets.ModelViewSet):
    queryset = ConsumpitionGoal.objects.all().order_by('-goal_initial')
    serializer_class = ConsumpitionGoalSerializer


class GoalsListSet(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, year):
        user = self.request.user
        year = datetime.date(int(year), 1, 1)

        goal = ConsumpitionGoal.timeseries.filter(
            user=user).year(year).monthly_closing

        # 1m^3 = 1000 liters
        month_dict = {g.goal_initial.month: g.goal
                for g in goal}

        response = {
            "customer_goals": [month_dict.get(m, None)
                for m in range(1, 13)],
        }

        return Response(response)
