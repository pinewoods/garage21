from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers

class WaterTank(models.Model):
    device_key = models.CharField(
            max_length=32, blank=True, unique=True, editable=False)
    user = models.ForeignKey(User, unique=False)
    total_height = models.FloatField(blank=False)
    air_gap = models.FloatField(blank=False)
    description = models.CharField(max_length=140, blank=True)

class SensorType(models.Model):
    code = models.CharField(max_length=64, blank=True, unique=True)
    description = models.CharField(max_length=256, blank=True)
    unit = models.CharField(max_length=16, blank=False)

class Reading(models.Model):
    water_tank = models.ForeignKey(WaterTank, unique=False)
    sensor_type = models.ForeignKey(SensorType, unique=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    sensor_reading = models.IntegerField(blank=False)

class ReadingSerializer(serializers.ModelSerializer):
    water_tank = serializers.PrimaryKeyRelatedField(read_only=True)
    sensor_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Reading
        fields = ('timestamp', 'sensor_reading')
