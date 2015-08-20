from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from water_meter.models import WaterTank
from water_meter.models import Reading

from sabesp.models import SabespReading
from sabesp.models import SabespProfile
from sabesp.models import Ticket

from sabesp.forms import UserProfileForm
from sabesp.forms import SabespProfileForm
from sabesp.forms import SupportForm


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

    context = {
        'user': user,
        'tanks': tanks,
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
    if request.method == 'GET':
        user = request.user
        profiles_sabesp = SabespProfile.objects.filter(user=user)
        tanks = WaterTank.objects.filter(user=user)

        print(type(user.profile))
        print(user.profile)

        user_profile_form = UserProfileForm(instance=user.profile)
        sabesp_forms = [SabespProfileForm(instance=instance)
                for instance in profiles_sabesp]

        context = {
            'user': user,
            'user_profile_form': user_profile_form,
            'sabesp_forms': sabesp_forms,
            'tanks': tanks,
        }

        return render(request,
                      'website/settings.html',
                      context=context)

    if request.method == 'POST':
        from IPython import embed; embed()

@login_required
def support(request):
    user = request.user

    if request.method == 'GET':
        support_form = SupportForm(instance=user.profile)

        context = {
            'user': user,
            'support_form': support_form,
        }    
    else:
        form = SupportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            description = form.cleaned_data['description']

            ticket = Ticket(user=user, support_code=tipo, description=description)
            ticket.save()

            context = {
            'user': user,
            'message': "Seu e-mail foi enviado com sucesso",
            } 
        else:
            context = {
            'user': user,
            'message': "Ocorreu entre em contato com nosso telefone (11)99999-9999",
            }

    return render(request,
                  'website/support.html',
                  context=context, form)
