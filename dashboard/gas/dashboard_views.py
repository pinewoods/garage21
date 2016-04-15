from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from gas.models import GasCylinder

class GasCylinderListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(GasCylinderListView, self).get_context_data(**kwargs)
        context['module_context'] = 'gas'
        return context

   def get_queryset(self):
        return GasCylinder.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GasCylinderListView, self).dispatch(
                request, *args, **kwargs)
