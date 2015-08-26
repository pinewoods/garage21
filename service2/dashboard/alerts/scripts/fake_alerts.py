"""
    Fake LevelAlerts for testing
    run: python manage.py runscript fake_alerts.py
"""

from django.core.exceptions import ObjectDoesNotExist
from notifications import notify

from alerts.models import LevelAlert
from water_meter.models import WaterTank


def run():

    tank = WaterTank.objects.get(pk=1)
    try:
        alert = LevelAlert.objects.filter(
                user=tank.user).latest('timestamp')
    except ObjectDoesNotExist:
        # Creates a object
        alert = LevelAlert(user=tank.user, level=50, active=True)
        alert.save()

    notify.send(tank.user,
            recipient=tank.user,
            verb=u'Testing Alerts',
            description='In a sort of ghastly simplicity we remove the'
            ' organ and demand the function'
            ' - C.S. Lewis, The Abolition of Man ')
