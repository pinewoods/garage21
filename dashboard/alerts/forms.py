from django import forms

from . import models

class LevelAlertForm(forms.ModelForm):

    class Meta:
        model = models.LevelAlert
        exclude = ('user',)
