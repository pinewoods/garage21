"""
    Random YFS201Reading for testing
    run: python manage.py runscript gen_yfs201.py
"""

import random
import datetime

from django.utils import timezone

from water_meter.models import WaterTank
from water_meter.models import HCSR04Reading

def run():

    tank = WaterTank.objects.get(pk=1)
    level = 17

    now = timezone.now()
    yesterday = now - datetime.timedelta(days=2)
    fifteen_minuts = datetime.timedelta(minutes=15)
    timestamp = yesterday

    #question = 'All Readings will be DELETED. Are you sure? (yes/no)? '
    #response = input(question)

    #if response != 'yes':
    #    return

    # Kill them all
    HCSR04Reading.objects.all().delete()

    objects = []
    while timestamp < now:
        obj = HCSR04Reading(water_tank=tank,
                            sensor_reading=level,
                            timestamp = timestamp)

        objects.append(obj)
        timestamp += fifteen_minuts
        level += random.gauss(0, 5)
        level = min(tank.total_height, max(level, tank.air_gap))

    HCSR04Reading.objects.bulk_create(objects)
