from django.db import models

class SensorReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    reading = models.IntegerField()
