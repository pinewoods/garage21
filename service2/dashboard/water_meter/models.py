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

    def __str__(self):
        return self.code

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('code', 'unit')

class Reading(models.Model):

    class Meta:
        abstract = True

    water_tank = models.ForeignKey(WaterTank, unique=False)
    sensor_type = models.ForeignKey(SensorType, unique=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    sensor_reading = models.FloatField(blank=False)

    def __str__(self):
        return "[%s] %s %s" % (
                self.timestamp, self.sensor_reading, self.sensor_type.unit)

class YFS201Reading(Reading):
    pass

class HCSR04Reading(Reading):
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
