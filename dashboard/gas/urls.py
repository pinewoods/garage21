from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'api/$', views.ViewGasEndpoint.as_view(), name='endpoint'),
]
