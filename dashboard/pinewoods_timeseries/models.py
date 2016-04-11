import time
import datetime
from random import random

from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .querysets import TimeseriesQuerySet
from .querysets import ts_min


class Channel(models.Model):
    token = models.CharField(max_length=8,
            default=lambda: make_password(random()).split('$')[3][:8])
    user = models.ForeignKey(User, unique=False)

    def is_token_valid(self, token):
        return token == self.token

# TODO: Not worth the trouble
class ChannelAssociatedMixin(models.Model):

    class Meta:
        abstract = True

    channel = models.ForeignKey(Channel, unique=False)


class Reading(models.Model):

    objects = models.QuerySet().as_manager()
    timeseries = TimeseriesQuerySet().as_manager()

    class Meta:
        abstract = True

    class Extra:
        # Required for TimeseriesQuerySet
        ts_field = 'timestamp'

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


class SparceReading(Reading):

    class Meta:
        abstract = True

    class Extra:
        # Required for TimeseriesQuerySet
        ts_field = 'timestamp'
        # Amount of move before writing data o the database
        deviation = 0.1

    def save(self, *args, **kwargs):
        last_reading = 0 # TODO
        drift = abs(last_reading - self.sensor_reading)
        if drift > self.Extra.deviation:
            super(Reading, self).save(*args, **kwargs)
        else:
            pass # TODO
