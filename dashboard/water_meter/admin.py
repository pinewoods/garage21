from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.WaterTank)
admin.site.register(models.ConsumpitionGoal)

class HCSR04ReadingAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Reading

admin.site.register(models.HCSR04Reading, HCSR04ReadingAdmin)

class YFS201ReadingAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Reading

admin.site.register(models.YFS201Reading, YFS201ReadingAdmin)
