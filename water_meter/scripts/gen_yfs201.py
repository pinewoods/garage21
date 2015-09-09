"""
    Random YFS201Reading for testing
    run: python manage.py runscript gen_yfs201.py
"""

import random
import datetime

from django.utils import timezone

from water_meter.models import WaterTank
from water_meter.models import YFS201Reading

def run():

    tank = WaterTank.objects.get(pk=1)
    flow_counter = 100.0

    now = timezone.now()
    last_month = now - datetime.timedelta(days=30)
    fifteen_minuts = datetime.timedelta(minutes=15)
    timestamp = last_month

    question = 'All Readings will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    # Kill them all
    YFS201Reading.objects.all().delete()

    objects = []
    while timestamp < now:
        obj = YFS201Reading(water_tank=tank,
                            sensor_reading=flow_counter,
                            timestamp = timestamp)

        objects.append(obj)
        timestamp += fifteen_minuts
        flow_counter += random.gauss(4.5, 6)

    YFS201Reading.objects.bulk_create(objects)
