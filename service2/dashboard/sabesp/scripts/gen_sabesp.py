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
    month = timezone.now().month

    question = 'All Sabesp Stuff will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    # Kill them all
    SabespReading.objects.all().delete()

    objects = []
    for m in range(1, month):
        competence = datetime.date(day=1, month=m, year=year)
        datestamp = datetime.date(day=15, month=m, year=year)

        obj = SabespReading(sabesp_profile=sabesp_profie,
                               sensor_id=hidrometro,
                               reading_m3=random.gauss(105, 10),
                               reading_competence=competence,
                               datestamp=datestamp)

        objects.append(obj)

    SabespReading.objects.bulk_create(objects)
