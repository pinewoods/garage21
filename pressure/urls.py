from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ViewReadings.as_view(), name='endpoint'),

    url(r'^current-temperature/$',
        views.ViewCurrentTemperature.as_view(),
        name='current-temperature'),

    url(r'^current-pressure/$',
        views.ViewCurrentPressure.as_view(),
        name='current-pressure'),

    url(r'^intraday-pressure/$',
        views.ViewIntradayPressure.as_view(),
        name='intraday-pressure'),

    url(r'^intraday-temperature/$',
        views.ViewIntradayTemperature.as_view(),
        name='intraday-temperature'),

    url(r'^intraday-pressure-temperature/$',
        views.ViewIntradayPressureTemperature.as_view(),
        name='intraday-pressure-temperature'),

]
