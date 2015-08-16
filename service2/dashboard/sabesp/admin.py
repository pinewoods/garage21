from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ConsumerType)
admin.site.register(models.SabespProfile)
admin.site.register(models.HidrometroSabesp)
admin.site.register(models.FeePrice)
admin.site.register(models.Taxe)
