from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from water_meter.models import WaterTank
from water_meter.models import Reading

from sabesp.models import SabespProfile
from sabesp.models import SabespReading
from sabesp.models import SabespProfileForm

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
    profile = SabespProfile.objects.filter(user=user)
    readings = SabespReading.objects.filter(sabesp_profile=profile)

    context = {
        'user': user,
        'readings': readings,
    }

    return render(request,
                  'website/historic.html',
                  context=context)

@login_required
def settings(request):
    if request.method == 'GET':
        user = request.user
        profiles = SabespProfile.objects.filter(user=user)
        tanks = WaterTank.objects.filter(user=user)

        print(profiles)
        profile_forms = [SabespProfileForm(instance=i) for i in profiles]

        context = {
            'user': user,
            'profile_forms': profile_forms,
            'tanks': tanks,
        }

        return render(request,
                      'website/settings.html',
                      context=context)

    if request.method == 'POST':
        from IPython import embed; embed()

