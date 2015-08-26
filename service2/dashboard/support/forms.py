from django import forms

from localflavor.br.forms import BRCNPJField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.forms import BRZipCodeField
from django.utils.translation import gettext as _

from . import models
from support.models import Ticket

# Create your views here.
SUPPORT_CHOICES = (
    ('BUG', 'Problema Técnico'),
    ('SUG', 'Sugestão'),
    ('REC', 'Reclamação'),
)

class SupportForm(forms.ModelForm):
    support_code = forms.ChoiceField(choices=SUPPORT_CHOICES)

    class Meta:
        model = Ticket
        fields = ['support_code','description']

        labels = {
                'support_code': 'Tipo',
                'description': 'Descrição',
        }
        error_messages = {
            'description': {'required': _("Por favor, insira uma descrição.")},
            'user': {'required': _("Por favor, informe seu usuário.")},
        }
