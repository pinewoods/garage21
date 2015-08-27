from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfile(models.Model):
    """
        Billing Profile
    """
    user = models.OneToOneField(User, related_name='profile')
    email = models.EmailField(blank=True, null=True)
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=16, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    cep = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.user.username


class ConsumerType(models.Model):
    code = models.CharField(max_length=10, blank=False)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return "%s - %s" % (self.code, self.description)


class SabespProfile(models.Model):
    user = models.ForeignKey(User, unique=False)
    rgi = models.FloatField(blank=False)
    customer_id = models.FloatField(blank=False)
    consumer_type = models.ForeignKey(ConsumerType, unique=False)
    # This is from which dam this water supply comes from 
    supply_unit = models.CharField(max_length=140, blank=True)
    consumption_goal = models.FloatField(blank=False)
    sabesp_read_day = models.FloatField(blank=False)
    
    def __str__(self):
        return self.user.username

class SabespProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=UserProfile.objects.all())

    class Meta:
        model = SabespProfile
        fields = ('user', 'rgi', 'customer_id',
                  'consumption_goal','sabesp_read_day')


class HidrometroSabesp(models.Model):
    sensor_id = models.CharField(max_length=64, blank=False, unique=True)
    sabesp_profile = models.ForeignKey(SabespProfile, unique=False)

    def __str__(self):
        return self.sensor_id

class FeePrice(models.Model):
    consumer_type = models.ForeignKey(ConsumerType, unique=False)
    price_m3 = models.FloatField(max_length=64, blank=False, unique=False)
    band = models.FloatField(max_length=64, blank=False, unique=False)

    def __str__(self):
        return "Tipo %s faixa: %s" % (self.consumer_type.code, self.band)

class Taxe(models.Model):
    code = models.CharField(max_length=64, blank=False, unique=True)
    consumer_type = models.ForeignKey(ConsumerType, unique=False)
    rate = models.FloatField(max_length=64, blank=False, unique=False)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.code

class SabespReading(models.Model):
    sabesp_profile = models.ForeignKey(SabespProfile, unique=False)
    sensor_id = models.ForeignKey(HidrometroSabesp, unique=False)
    reading_m3 = models.FloatField(max_length=64, blank=False, unique=False)
    reading_competence = models.DateField()

    def __str__(self):
        return "%s : %s" % (self.reading_competence, self.sensor_id)


class SabespReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SabespReading
        fields = ('reading_m3','reading_competence')

