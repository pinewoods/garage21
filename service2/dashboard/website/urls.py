from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        pattern_name='dashboard', permanent=False)),
    url(r'^dashboard/$', views.index, name='dashboard'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^historic/$', views.historic, name='historic'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^support/$', views.support, name='support'),
]
