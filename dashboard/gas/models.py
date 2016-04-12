from django.db import models
from django.contrib.auth.models import User

from jsonfield import JSONField

from pinewoods_timeseries.models import Channel
from pinewoods_timeseries.models import SparceReading

class GasCylinder(Channel):

    P45 = 'P45'
    P90 = 'P90'
    P190 = 'P190'

    CYLINDER_CHOICES = (
            (P45, ('P-45')),
            (P90, ('P-90')),
            (P190, ('P-190')),
    )


    location = JSONField()

    cyclinder_type = models.CharField(
        max_length=4,
        choices=CYLINDER_CHOICES)


class CylinderWeight(SparceReading):
    channel = models.ForeignKey(GasCylinder, unique=False)
