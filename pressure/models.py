import time
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import serializers

from water_meter.models import Reading

class LD9PressureReading(Reading):

    @property
    def sensor_type(self):
        return 'LD9'

    @property
    def unit(self):
        return 'bar'


class LD9TemperatureReading(Reading):

    @property
    def sensor_type(self):
        return 'LD9'

    @property
    def unit(self):
        return 'ºC'


class PressureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LD9PressureReading
        fields = ('sensor_type', 'timestamp', 'unix_timestamp', 'sensor_reading')


class EssentialPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LD9PressureReading
        fields = ('unix_timestamp', 'sensor_reading')


class TemperatureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LD9TemperatureReading
        fields = ('sensor_type', 'timestamp', 'unix_timestamp', 'sensor_reading')


class EssentialTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LD9TemperatureReading
        fields = ('unix_timestamp', 'sensor_reading')

