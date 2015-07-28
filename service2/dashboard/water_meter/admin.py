from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.WaterTank)
admin.site.register(models.Reading)
admin.site.register(models.Flow)