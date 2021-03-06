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
                'rgi': 'RGI (Registro Geral de Instalacao)',
                'customer_id': 'Codigo do Cliente',
                'consumer_type': 'Tipo de Ligacao',
                'supply_unit': 'Reservatorio',
                'consumption_goal': 'Meta Sabesp',
                'sabesp_read_day': 'Dia da Leitura Sabesp',
        }


class SabespReadingForm(forms.ModelForm):

    class Meta:
        model = models.SabespReading
        fields = '__all__'
        labels = {
            'sensor_id': 'Codigo Hidrometro Sabesp',
            'reading_m3': 'Leitura Atual',
            'reading_competence': 'Mes de Competencia',
            'datestamp': 'Dia da Leitura',
        }

        widgets = {
            'reading_competence': forms.DateInput(attrs={'type':'hidden','required': True}),
        }

        error_messages = {
            'reading_competence': {'required': ("Por favor, escolha o mesmo para iniciar a meta.")},
            'datestamp': {'required': ("Por favor, escolha o mesmo para iniciar a meta.")},
        }
