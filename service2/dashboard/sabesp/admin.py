from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from . import models
from . import forms

admin.site.unregister(User)
admin.site.unregister(Group)

# TODO: Factor out
class UserProfileAdminInline(admin.StackedInline):
    model = models.UserProfile
    form = forms.UserProfileForm
    can_delete = False

# TODO: Factor out
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileAdminInline]

admin.site.register(User, UserProfileAdmin)

# sabesp/models
admin.site.register(models.ConsumerType)
admin.site.register(models.SabespProfile)
admin.site.register(models.SabespWatermeter)
admin.site.register(models.FeePrice)
admin.site.register(models.Tax)
admin.site.register(models.SabespReading)
