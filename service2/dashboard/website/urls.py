from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.index, name='dashboard'),
    url(r'^goals/$', views.goals, name='goals'),
]
