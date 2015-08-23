from django import forms

from localflavor.br.forms import BRCNPJField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.forms import BRZipCodeField
from django.utils.translation import gettext as _

from . import models
from support.models import Ticket

class UserProfileForm(forms.ModelForm):
    cnpj = BRCNPJField(label="CNPJ")
    phone = BRPhoneNumberField(required=False, label="Telefone")
    mobile = BRPhoneNumberField(required=False, label="Celular")
    cep = BRZipCodeField(required=False, label="CEP")

    class Meta:
        model = models.UserProfile
        fields = '__all__'

class SabespProfileForm(forms.ModelForm):
    class Meta:
        model = models.SabespProfile
        fields = '__all__'

        labels = {
                'rgi': 'RGI (Registro Geral de Instalação)',
                'customer_id': 'Código do Cliente',
                'consumer_type': 'Tipo de Ligação',
                'supply_unit': 'Reservatório',
                'consumption_goal': 'Meta Sabesp',
        }

SUPPORT_CHOICES = (
    ('BUG', 'Problema Técnico'),
    ('SUG', 'Sugestão'),
    ('REC', 'Reclamação'),
)

class SupportForm(forms.ModelForm):
    support_code = forms.ChoiceField(choices=SUPPORT_CHOICES)

    class Meta:
        model = Ticket
        fields = ['user','support_code','description']

        labels = {
                'user': 'Usuário',
                'support_code': 'Tipo',
                'description': 'Descrição',
        }
        error_messages = {
            'description': {'required': _("Por favor, insira uma descrição.")},
            'user': {'required': _("Por favor, informe seu usuário.")},
        }