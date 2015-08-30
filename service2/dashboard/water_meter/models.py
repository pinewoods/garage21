import time
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

    @property
    def unix_timestamp(self):
        #TODO: datetime.utcfromtimestamp()
        return time.mktime(self.timestamp.timetuple())


class YFS201Reading(Reading):
    @property
    def sensor_type(self):
        return 'YF-S201'

    @property
    def unit(self):
        return 'liters'


class YFS201ReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = YFS201Reading
        fields = ('timestamp', 'sensor_reading')


class HCSR04Reading(Reading):
    @property
    def sensor_type(self):
        return 'HC-SR04'

    @property
    def unit(self):
        return 'cm'

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
                  'timestamp', 'unix_timestamp', 'level')


class EssentialHCSR04Serializer(serializers.ModelSerializer):
    class Meta:
        model = HCSR04Reading
        fields = ('unix_timestamp', 'level')


class ConsumpitionGoal(models.Model):
    user = models.ForeignKey(User, unique=False,blank=False)
    goal_initial = models.DateField(blank=False)
    goal = models.FloatField(blank=False)

    def __str__(self):
        return "%s" % (self.goal_initial)


class ConsumpitionGoalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all())

    class Meta:
        model = ConsumpitionGoal
        fields = ('user','goal_initial', 'goal')


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsumpitionGoal
        fields = ('goal','goal_initial')
