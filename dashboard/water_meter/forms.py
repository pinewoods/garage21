from django import forms
from django.forms.extras.widgets import SelectDateWidget

from django.utils.translation import gettext as _

from . import models
from water_meter.models import ConsumpitionGoal

# Create your views here.

class ConsumptionGoalForm(forms.ModelForm):

    widget=SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"))

    class Meta:
        model = ConsumpitionGoal
        fields = ['goal_initial','goal']

        labels = {
                'goal': 'Meta',
        }
        widgets = {
            'goal_initial': forms.DateInput(attrs={'type':'hidden','required': True}),
        }
        error_messages = {
            'goal': {'required': _("Por favor, insira uma meta."),'invalid': _("Por favor, insira uma meta válida.")},
            'goal_initial': {'required': _("Por favor, escolha o mesmo para iniciar a meta.")},
        }
