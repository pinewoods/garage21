from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from . import models
from . import forms

admin.site.unregister(User)
admin.site.unregister(Group)


class UserProfileAdminInline(admin.StackedInline):
    model = models.UserProfile
    form = forms.UserProfileForm
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileAdminInline]

admin.site.register(User, UserProfileAdmin)
admin.site.register(models.ConsumerType)
admin.site.register(models.SabespProfile)
admin.site.register(models.HidrometroSabesp)
admin.site.register(models.FeePrice)
admin.site.register(models.Taxe)
