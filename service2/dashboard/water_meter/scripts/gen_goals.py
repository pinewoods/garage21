"""
    Random ConsumpitionGoal for testing
    run: python manage.py runscript gen_goals.py
"""

import random
import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from water_meter.models import ConsumpitionGoal

def run():

    user = User.objects.get(pk=1)
    year = timezone.now().year

    question = 'All Goals will be DELETED. Are you sure? (yes/no)? '
    response = input(question)

    if response != 'yes':
        return

    # Kill them all
    ConsumpitionGoal.objects.all().delete()

    objects = []
    for month in range(1, 13):
        goal_initial = datetime.date(day=1, month=month, year=year)

        obj = ConsumpitionGoal(user=user,
                               goal_initial=goal_initial,
                               goal=random.gauss(100, 10))

        objects.append(obj)

    ConsumpitionGoal.objects.bulk_create(objects)
