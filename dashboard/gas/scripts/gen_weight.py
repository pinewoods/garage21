"""
    Random CylinderWeight for testing
    run: python manage.py runscript gen_weight
"""

import random
import datetime

from django.utils import timezone

from gas.models import GasCylinder
from gas.models import CylinderWeight

def run():

    cylinders = GasCylinder.objects.filter(user__username='admin')

    now = timezone.now()
    yesterday = now - datetime.timedelta(days=2)
    fifteen_minuts = datetime.timedelta(minutes=15)
    timestamp = yesterday

    question = 'All Readings will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    objects = []
    for c in cylinders:

        # Kill them all
        CylinderWeight.objects.filter(channel=c).delete()

        # Reset state
        level = random.uniform(85, 100)
        timestamp = yesterday

        while timestamp < now:
            obj = CylinderWeight(channel=c,
                                sensor_reading=level,
                                timestamp=timestamp)

            objects.append(obj)
            timestamp += fifteen_minuts
            level -= random.gauss(0, 1)
            level = max(0, min(level, 100))

    CylinderWeight.objects.bulk_create(objects)
    print('%d Objects created' % len(objects))
