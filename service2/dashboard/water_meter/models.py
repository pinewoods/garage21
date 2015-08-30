import time
import pytz
import datetime
import calendar
import collections
from bisect import bisect_left

from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import serializers


# Useful functions.

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


class TimeseriesQuerySet(QuerySet):

    def year(self, timestamp):
        year = timestamp.year

        jan_1st = datetime.datetime.combine(
                datetime.datetime(year, 1, 1), datetime.time.min)

        dec_31st = datetime.datetime.combine(
                datetime.datetime(year, 12, 31), datetime.time.max)

        return self.filter(
            timestamp__range=(
                jan_1st, dec_31st)).order_by('timestamp')

    def month(self, timestamp):
        year, month = timestamp.year, timestamp.year
        mb = MonthBoundary(year, month)
        return self.filter(
                timestamp__range=(
                    mb.first, mb.last)).order_by('timestamp')

    def day(self, timestamp):
        return self.filter(
            timestamp__range=(
                datetime.datetime.combine(timestamp, datetime.time.min),
                datetime.datetime.combine(timestamp, datetime.time.max))
            ).order_by('timestamp')


# Models start here.

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

    objects = models.QuerySet().as_manager()
    timeseries = TimeseriesQuerySet().as_manager()

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
