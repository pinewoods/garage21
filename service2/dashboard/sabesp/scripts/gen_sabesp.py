"""
    Random SabespReading for testing
    run: python manage.py runscript gen_goals.py
"""

import random
import datetime

from django.utils import timezone

from sabesp.models import ConsumerType
from sabesp.models import SabespProfile
from sabesp.models import HidrometroSabesp
from sabesp.models import SabespReading


def run():

    sabesp_profie = SabespProfile.objects.get(pk=1)
    hidrometro = HidrometroSabesp.objects.get(pk=1)
    year = timezone.now().year

    question = 'All Sabesp Stuff will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    # Kill them all
    SabespReading.objects.all().delete()

    objects = []
    for month in range(1, 12):
        competence = datetime.date(day=1, month=month, year=year)

        obj = SabespReading(sabesp_profile=sabesp_profie,
                               sensor_id=hidrometro,
                               reading_m3=random.gauss(16, 5),
                               reading_competence=competence)

        objects.append(obj)

    SabespReading.objects.bulk_create(objects)
