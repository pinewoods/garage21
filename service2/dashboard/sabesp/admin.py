from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from . import models
from . import forms

admin.site.unregister(User)
admin.site.unregister(Group)


class ProfileAdminInline(admin.StackedInline):
    model = models.Profile
    form = forms.ProfileForm
    can_delete = False

class ProfileAdmin(UserAdmin):
    inlines = [ProfileAdminInline]

admin.site.register(User, ProfileAdmin)
admin.site.register(models.ConsumerType)
admin.site.register(models.SabespProfile)
admin.site.register(models.HidrometroSabesp)
admin.site.register(models.FeePrice)
admin.site.register(models.Taxe)
