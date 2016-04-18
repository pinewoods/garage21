from django.conf.urls import include, url
from . import api_views
from . import dashboard_views

urlpatterns = [
    url(r'api/$', api_views.ViewGasEndpoint.as_view(), name='endpoint'),

    url(r'api/gas_cylinder/(?P<channel>[0-9]+)/current-weight/$',
        api_views.ViewCurrentWeight.as_view(),
        name='current-weight'),

    url(r'dashboard/list/$',
        dashboard_views.GasCylinderListView.as_view(),
        name='gas-cylinder-list'),
]
