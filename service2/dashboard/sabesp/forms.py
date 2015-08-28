from django import forms

from localflavor.br.forms import BRCNPJField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.forms import BRZipCodeField

from . import models

class UserProfileForm(forms.ModelForm):
    cnpj = BRCNPJField(label="CNPJ")
    phone = BRPhoneNumberField(required=False, label="Telefone")
    mobile = BRPhoneNumberField(required=False, label="Celular")
    cep = BRZipCodeField(required=False, label="CEP")

    class Meta:
        model = models.UserProfile
        exclude = ('user',)

class SabespProfileForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = models.SabespProfile
        exclude = ('user',)

        labels = {
                'rgi': 'RGI (Registro Geral de Instalação)',
                'customer_id': 'Código do Cliente',
                'consumer_type': 'Tipo de Ligação',
                'supply_unit': 'Reservatório',
                'consumption_goal': 'Meta Sabesp',
                'sabesp_read_day': 'Dia da Leitura Sabesp',
        }

