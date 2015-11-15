from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.mail import send_mail
from notifications import notify

from .models import LevelAlert
from water_meter.models import HCSR04Reading


@receiver(post_save, sender=HCSR04Reading)
def levelAlertHandler(sender, instance, created, raw, **kwargs):
    # created = not updated
    # raw means fixture loaded objects
    if not created or raw:
        return

    user = instance.water_tank.user
    alert = LevelAlert.objects.filter(user=user).latest('timestamp')

    # TODO: check if alert does not exists
    if not alert:
        return

    if alert.level > instance.level:
        print("Send Email")
        # send_mail('Subject here', 'Here is the message.',
        #       'from@example.com', ['to@example.com'], fail_silently=False)

        msg = u'O nivel do reservatorio esta abaixo de %.1f%%'
        notify.send(user,
                recipient=user, verb=u'O nivel esta baixo!',
                action_object=instance,
                description=msg % instance.level)
