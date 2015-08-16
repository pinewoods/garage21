from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from water_meter.models import WaterTank
from water_meter.models import Reading
from sabesp.models import *

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
    user = request.user
    profile = SabespProfile.objects.filter(user=user)
    tanks = WaterTank.objects.filter(user=user)

    context = {
        'user': user,
        'profile': profile,
        'tanks': tanks,
    }

    return render(request,
                  'website/settings.html',
                  context=context)
