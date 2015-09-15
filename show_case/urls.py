from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        pattern_name='showcase', permanent=False)),
    url(r'^showcase/$', views.index, name='showcase'),
    url(r'^support2/$', views.support, name='support2'),
]
