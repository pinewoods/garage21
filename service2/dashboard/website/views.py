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
                  'website/index.html',
                  context=context)

@login_required
def goals(request):
    user = request.user
    tanks = WaterTank.objects.filter(user=user)

    if request.method == 'GET':

        goals_form = ConsumptionGoalForm(initial={'user': user})

        context = {
            'user': user,
            'tanks': tanks,
            'goals_form': goals_form,
        }
    if request.method == 'POST':
        goals_form = ConsumptionGoalForm(request.POST)
        message = ''
        # check whether it's valid:
        if goals_form.is_valid():
            goal_initial = goals_form.cleaned_data['goal_initial']
            goal = goals_form.cleaned_data['goal']

            consumptionGoal = ConsumpitionGoal(user=user, goal_initial=goal_initial, goal=goal)
            consumptionGoal.save()

            message = "Sua meta foi inserida com sucesso"

        context = {
            'user': user,
            'tanks': tanks,
            'message': message,
            'goals_form': goals_form,
        }
    return render(request,
                  'website/goals.html',
                  context=context)

@login_required
def historic(request):
    user = request.user
    profile = SabespProfile.objects.get(user=user)

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request,
                  'website/historic.html',
                  context=context)

@login_required
def settings(request):

    user = request.user
    tanks = WaterTank.objects.filter(user=user)

    profiles_sabesp = SabespProfile.objects.filter(user=user)
    # TODO get each tank's alert
    alerts = LevelAlert.objects.filter(user=user).latest('timestamp')

    user_profile_form = UserProfileForm(instance=user.profile)
    sabesp_forms = [SabespProfileForm(instance=instance)
            for instance in profiles_sabesp]
    # TODO
    alert_forms = [LevelAlertForm(instance=alerts)]

    if request.method == 'POST':
        # TODO: Redirect each submit to its own url action
        if 'user_profile' in request.POST:
            form = user_profile_form = UserProfileForm(request.POST,
                    instance=user.profile)
        if 'sabesp_profile' in request.POST:
            sabesp_instance = profiles_sabesp.get(
                    id=int(request.POST['id']))
            form = sabesp_form = SabespProfileForm(request.POST,
                    instance=sabesp_instance)
            sabesp_forms = [sabesp_form] # Gambi
        if 'alert' in request.POST:
            form = alert_form = LevelAlertForm(request.POST)
            alert_forms = [alert_form] # Gambi

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

    context = {
        'user': user,
        'user_profile_form': user_profile_form,
        'sabesp_forms': sabesp_forms,
        'alert_forms': alert_forms,
        'tanks': tanks,
    }

    return render(request,
                  'website/settings.html',
                  context=context)


@login_required
def support(request):

    user = request.user
    message = ''

    if request.method == 'GET':
        support_form = SupportForm(initial={'user': user})

        context = {
            'user': user,
            'support_form': support_form,
        }

    if request.method == 'POST':

        support_form = SupportForm(request.POST)
        # check whether it's valid:
        if support_form.is_valid():
            tipo = support_form.cleaned_data['support_code']
            description = support_form.cleaned_data['description']

            ticket = Ticket(user=user, support_code=tipo, description=description)
            ticket.save()

            message = "Seu ticket foi gerado com sucesso"

    context = {
        'user': user,
        'message': message,
        'support_form': support_form,
    }

    return render(request,
                  'website/support.html',
                  context=context)
