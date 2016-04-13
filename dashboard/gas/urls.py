from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', include('gas.gas_urls')),
    url(r'api/^$', include('gas.api_urls')),
]
