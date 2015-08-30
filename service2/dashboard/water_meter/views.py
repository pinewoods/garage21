import datetime
import calendar
import collections
from bisect import bisect_left

import pytz

from django.db.models.query import QuerySet
from django.http import Http404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from .models import  YFS201Reading
from .models import  HCSR04Reading
from .models import  HCSR04ReadingSerializer
from .models import  YFS201ReadingSerializer
from .models import  EssentialHCSR04Serializer
from .models import  WaterTank
from .models import  ConsumpitionGoal
from .models import  ConsumpitionGoalSerializer
from .models import  GoalSerializer


def each_last_reading(readings, first_day, last_day):
    """
        Returns the last reading of each day in range.

        * This functions uses the bisection algorithm,
        so `readings` must be sorted!
        * Each object in `readings` must support __lt__
        * Only on Python 3.6 bisect will support key=
    """
    list(readings).sort(key=lambda x: x.timestamp)
    current_day = first_day
    one_day = datetime.timedelta(days=1)

    days_set = collections.OrderedDict()
    while last_day > current_day:
        # Get the first value before current_day
        index = bisect_left(readings, current_day)
        if index:
            days_set[index-1] = readings[index-1]
        current_day += one_day

    return days_set.values()

def MonthBoundary(year, month):
    """
        Returns the first and the last datatime.datetime
        from a given month.
    """
    y, m = int(year), int(month)
    days = calendar.monthrange(y, m)

    first = datetime.date(year=y, month=m, day=1)
    last = datetime.date(year=y, month=m, day=days[-1])

    ti = datetime.datetime.combine(first, datetime.time.min)
    tf = datetime.datetime.combine(last, datetime.time.max)

    month_boundaries = collections.namedtuple('MonthBoundary',
            ['first', 'last'])

    return month_boundaries(pytz.utc.localize(ti),
                            pytz.utc.localize(tf))

class ViewReadings(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)

    def post(self, request, format=None):
        """
        Recives data from sensors.
        """
        wt = WaterTank.objects.get(pk=1)

        level_reading = HCSR04Reading(
                sensor_reading=request.data['echo'],
                water_tank=wt)

        flow_reading = YFS201Reading(
                sensor_reading=request.data['total_liters'],
                water_tank=wt)

        level_reading.save()
        flow_reading.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCurrentTankLevel(RetrieveAPIView):
    lookup_field = 'water_tank'
    serializer_class = HCSR04ReadingSerializer

    # Copied from Source ...
    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """

        # Modified... no queryset here

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        # Modified... custom queryset
        try:
            obj = HCSR04Reading.objects.filter(
                **filter_kwargs).order_by('timestamp').last()

        except (TypeError, ValueError):
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

class ViewIntradayTankLevel(ListAPIView):
    lookup_field = 'water_tank'
    serializer_class = EssentialHCSR04Serializer
    queryset = HCSR04Reading.objects.filter(
            timestamp__gt=datetime.datetime.combine(
                    datetime.date.today(), datetime.time.min)
                        ).order_by('-timestamp')

class ViewMonthlyGoals(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, water_tank, year, month):
        """
            Return data for the monthly goals burndown chart.
        """
        mb = MonthBoundary(year, month)

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

        readings = YFS201Reading.objects.filter(water_tank=wt,
                timestamp__range=(mb.first, mb.last)).order_by('timestamp')

        r = each_last_reading(readings, mb.first, mb.last)
        # 1m^3 = 1000 liters
        consumption = [(c.read() - readings[0].read()) / 1000. for c in r]

        days_count = mb.last.day

        response = {
                "sabesp_goal": sabesp_goal,
                "sabesp_step": sabesp_goal / days_count,
                "pinewoods_goal": pinewoods_goal,
                "pinewoods_step": pinewoods_goal / days_count,
                "days_count": days_count,
                "consumption": consumption,
         }

        return Response(response)

class ViewMonthlyReadings(ListAPIView):
    serializer_class = YFS201ReadingSerializer

    def get_queryset(self):
        user = self.request.user
        wt = WaterTank.objects.filter(user=user)
        year = int(self.kwargs['year'])

        return YFS201Reading.objects.filter(water_tank=wt, timestamp__year=year).order_by('timestamp')


class GoalsViewSet(viewsets.ModelViewSet):
    queryset = ConsumpitionGoal.objects.all().order_by('-goal_initial')
    serializer_class = ConsumpitionGoalSerializer


class GoalsListSet(ListAPIView):
    serializer_class = GoalSerializer

    def get_queryset(self):
        user = self.request.user
        year = int(self.kwargs['year'])
        return Cabesp_goalnsumpitionGoal.objects.filter(user=user, goal_initial__year=year).order_by('goal_initial')
