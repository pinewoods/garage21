from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from water_meter.models import WaterTank
from water_meter.models import Reading

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
