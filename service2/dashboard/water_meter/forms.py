from django import forms

from django.utils.translation import gettext as _

from . import models
from water_meter.models import ConsumpitionGoal

# Create your views here.

class ConsumptionGoalForm(forms.ModelForm):

    class Meta:
        model = ConsumpitionGoal
        fields = ['user', 'goal_initial','goal']

        labels = {
                'user': 'Usuário',
                'goal_initial': 'Mês inicial',
                'goal': 'Descrição',
        }
        widgets = {
            'goal_initial': forms.DateInput(attrs={'class':'datepicker'}),
        }
        error_messages = {
            'goal': {'required': _("Por favor, insira uma meta.")},
            'goal': {'invalid': _("Por favor, insira uma meta válida.")},
            'user': {'required': _("Por favor, informe seu usuário.")},
            'goal_initial': {'required': _("Por favor, escolha o mesmo para iniciar a meta.")},
        }