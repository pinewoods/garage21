import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

from django.contrib.auth.models import User


class LevelAlert(models.Model):
    user = models.ForeignKey(User, unique=False)
    level = models.FloatField(validators = [
        MinValueValidator(0.0), MaxValueValidator(100.0)])
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    active = models.BooleanField(default=False)
