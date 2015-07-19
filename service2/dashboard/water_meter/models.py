from django.db import models
from django.contrib.auth.models import User


class WaterTank(models.Model):
    device_key = models.CharField(
            max_length=32, blank=True, unique=True, editable=False)
    user = models.ForeignKey(User, unique=False)
    total_height = models.FloatField(blank=False)
    air_gap = models.FloatField(blank=False)
    description = models.CharField(max_length=140, blank=True)

class Reading(models.Model):
    water_tank = models.ForeignKey(WaterTank, unique=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    sensor_reading = models.IntegerField(blank=False, editable=False)
