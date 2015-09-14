from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from water_meter.models import WaterTank
from water_meter.models import Reading
from water_meter.models import ConsumpitionGoal
from sabesp.models import SabespReading
from sabesp.models import SabespProfile
from support.models import Ticket
from alerts.models import LevelAlert

from sabesp.forms import UserProfileForm
from sabesp.forms import SabespProfileForm
from support.forms import SupportForm
from sabesp.forms import SabespReadingForm
from water_meter.forms import ConsumptionGoalForm
from alerts.forms import LevelAlertForm


@login_required
def index(request):
    user = request.user
    tanks = WaterTank.objects.filter(user=user)

    context = {
        'user': user,
        'tanks': tanks,
    }

    return render(request,
                  'show_case/index.html',
                  context=context)


@login_required
def support(request):

    user = request.user
    context = {
        'user': user,
    }

    if request.method == 'GET':
        support_form = SupportForm(initial={'user': user})

    if request.method == 'POST':
        support_form = SupportForm(request.POST)
        # check whether it's valid:
        if support_form.is_valid():
            tipo = support_form.cleaned_data['support_code']
            description = support_form.cleaned_data['description']

            ticket = Ticket(user=user, support_code=tipo, description=description)
            ticket.save()

            context['dismissable_alert'] = 'Seu ticket foi gerado com sucesso'
            context['dismissable_alert_level'] = 'success'

    context['support_form'] = support_form

    return render(request,
                  'showcase/support.html',
                  context=context)
