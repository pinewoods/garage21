from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from . import views
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', RedirectView.as_view(
    #    pattern_name='dashboard', permanent=False)),

    # TODO: Fake reports
    url(r'^reports/$',
        TemplateView.as_view(template_name='website/reports.html'),
        name='reports'),

    url(r'^$', views.index, name='dashboard'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^historic/$', views.historic, name='historic'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^support/$', views.support, name='support'),
]
