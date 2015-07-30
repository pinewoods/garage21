from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.WaterTank)
admin.site.register(models.SensorType)
admin.site.register(models.Reading)
