"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'goals', views.GoalsViewSet, 'goals')
# name='goals-list'
# name='goals-detail'

urlpatterns = [
    #url(r'^$', views.ViewReadings.as_view(), name='endpoint'),
    url(r'^$', views.root_endpoint, name='endpoint'),
    url(r'^', include(router.urls)),
    url(r'^tank/(?P<water_tank>[0-9]+)/current-level/$',
            views.ViewCurrentTankLevel.as_view(),
            name='current-level'),
    url(r'^tank/(?P<water_tank>[0-9]+)/intraday-level/$',
            views.ViewIntradayTankLevel.as_view(),
            name='intraday-level'),
    url(r'^tank/(?P<water_tank>[0-9]+)/monthly-goals/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.ViewMonthlyGoals.as_view(),
            name='monthly-goals'),
    url(r'^consume-readings/year/(?P<year>[0-9]{4})/$',
            views.ViewMonthlyReadings.as_view(),
            name='consume-readings'),
    url(r'^goals/year/(?P<year>[0-9]{4})/$', views.GoalsListSet.as_view(),name='user-goals'),
]
