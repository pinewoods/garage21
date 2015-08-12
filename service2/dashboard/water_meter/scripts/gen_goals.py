"""
    Random ConsumpitionGoal for testing
    run: python manage.py runscript gen_goals.py
"""

import random
import datetime

from django.utils import timezone

from water_meter.models import WaterTank
from water_meter.models import SensorType
from water_meter.models import ConsumpitionGoal

def run():

    tank = WaterTank.objects.get(pk=1)
    flow_counter = 100.0
    year = timezone.now().year

    question = 'All Goals will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    # Kill them all
    ConsumpitionGoal.objects.all().delete()

    objects = []
    for month in range(1, 12):
        begin = datetime.date(day=1, month=month, year=year)
        end = datetime.date(day=1, month=month+1, year=year)

        obj = ConsumpitionGoal(water_tank=tank,
                               begin_date=begin,
                               end_date=end,
                               goal=6000,
                               real_consume=random.gauss(6000, 1000),
                               est_consume=random.gauss(6000, 1000))

        objects.append(obj)

    ConsumpitionGoal.objects.bulk_create(objects)
