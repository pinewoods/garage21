from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, unique=False)
    support_code = models.CharField(max_length=3, blank=False, unique=False)
    description = models.TextField(blank=False)