import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import serializers


class WaterTank(models.Model):
    device_key = models.CharField(
            max_length=32, blank=True, unique=True, editable=False)
    user = models.ForeignKey(User, unique=False)
    total_height = models.FloatField(blank=False)
    air_gap = models.FloatField(blank=False)
    description = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return "[%s] %s" % (self.user.username, self.description)


class SensorType(models.Model):
    code = models.CharField(max_length=64, blank=True, unique=True)
    description = models.CharField(max_length=256, blank=True)
    unit = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return self.code


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('code', 'unit', 'description')


class Reading(models.Model):
    class Meta:
        abstract = True

    water_tank = models.ForeignKey(WaterTank, unique=False)
    timestamp = models.DateTimeField(
                default=timezone.now, editable=False)
    sensor_reading = models.FloatField(blank=False)
    read = lambda self: self.sensor_reading # shortcut

    def __str__(self):
        return "[%s] %s" % (self.timestamp, self.sensor_reading)

    def __lt__(self, other):
        if isinstance(other, datetime.datetime):
            return self.timestamp < other
        else:
            return self.timestamp < other.timestamp


class YFS201Reading(Reading):
    @property
    def sensor_type(self):
        return 'YF-S201'


class HCSR04Reading(Reading):
    @property
    def sensor_type(self):
        return 'HC-SR04'

    @property
    def level(self):
        n = self.water_tank.total_height - self.sensor_reading
        d = self.water_tank.total_height - self.water_tank.air_gap
        return 100.0 * (n/d)


class HCSR04ReadingSerializer(serializers.ModelSerializer):
    water_tank = serializers.PrimaryKeyRelatedField(read_only=True)
    sensor_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = HCSR04Reading
        fields = ('water_tank', 'sensor_type',
                  'timestamp', 'level')


class ConsumpitionGoal(models.Model):
    water_tank = models.ForeignKey(WaterTank, unique=False)
    begin_date = models.DateField()
    end_date = models.DateField()
    goal = models.FloatField(blank=False)
    real_consume = models.FloatField(editable=False, null=True)
    est_consume = models.FloatField(editable=False, null=True)

    def __str__(self):
        return "[%s] %s" % (self.end_date, self.goal)


class ConsumpitionGoalSerializer(serializers.ModelSerializer):
    water_tank = serializers.PrimaryKeyRelatedField(
            queryset=WaterTank.objects.all())

    class Meta:
        model = ConsumpitionGoal
        fields = ('water_tank', 'begin_date', 'end_date',
                  'goal', 'real_consume', 'est_consume')
