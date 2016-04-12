from django.contrib import admin

# Register your models here.
from . import models

from pinewoods_timeseries.models import Channel
from pinewoods_timeseries.models import SparceReading

class GasCylinderAdmin(admin.ModelAdmin):
    class Meta:
        model = Channel

admin.site.register(models.GasCylinder, GasCylinderAdmin)

class CylinderWeightAdmin(admin.ModelAdmin):
    class Meta:
        model = models.SparceReading

admin.site.register(models.CylinderWeight, CylinderWeightAdmin)
