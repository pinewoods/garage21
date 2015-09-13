import datetime
import calendar
import collections
from bisect import bisect_left

import pytz

from django.db.models.query import QuerySet
from django.db.models import Max
from django.http import Http404

import rest_framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from .models import LD9PressureReading
from .models import LD9TemperatureReading
from .models import TemperatureReadingSerializer
from .models import PressureReadingSerializer


class ViewReadings(APIView):

    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (rest_framework.permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Recives data from sensors.
        """

        temp_reading = LD9TemperatureReading(
                sensor_reading=request.data['temp'])

        pressure_reading = LD9PressureReading(
                sensor_reading=request.data['pressao'])

        temp_reading.save()
        pressure_reading.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCurrentTemperature(APIView):

    renderer_classes = (JSONRenderer, )
    permission_classes = (rest_framework.permissions.AllowAny,)

    def get(self, request):
        temp_reading = LD9TemperatureReading.objects.all().latest('timestamp')
        serializer = TemperatureReadingSerializer(temp_reading)
        return Response(serializer.data)


class ViewCurrentPressure(APIView):

    renderer_classes = (JSONRenderer, )
    permission_classes = (rest_framework.permissions.AllowAny,)

    def get(self, request):
        temp_reading = LD9PressureReading.objects.all().latest('timestamp')
        serializer = PressureReadingSerializer(temp_reading)
        return Response(serializer.data)


class ViewIntradayTemperature(APIView):

    renderer_classes = (JSONRenderer, )
    permission_classes = (rest_framework.permissions.AllowAny,)

    def get(self, request):
        temp_reading = LD9TemperatureReading.objects.all()

        ts_list = []
        r_list = []
        for t in temp_reading:
            ts_list.append(t.timestamp)
            r_list.append(t.read())

        response = {
            "ts_list": ts_list,
            "r_list": r_list,
        }

        return Response(response)


class ViewIntradayPressure(APIView):

    renderer_classes = (JSONRenderer, )
    permission_classes = (rest_framework.permissions.AllowAny,)

    def get(self, request):
        temp_reading = LD9PressureReading.objects.all()

        ts_list = []
        r_list = []
        for t in temp_reading:
            ts_list.append(t.timestamp)
            r_list.append(t.read())

        response = {
            "ts_list": ts_list,
            "r_list": r_list,
        }

        return Response(response)
