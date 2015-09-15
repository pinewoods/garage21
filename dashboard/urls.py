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
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

import notifications

urlpatterns = [
    url(r'^sabesp/', include('sabesp.urls')),
    url(r'', include('show_case.urls')),
    url(r'', include('website.urls')),
    url(r'^accounts/login/', login,
        {'template_name': 'admin/login.html'}, name='login'),
    url(r'^accounts/logout/', logout,
        {'next_page': '/accounts/login'}, name='logout'),
    url(r'^api/', include('water_meter.urls')),
    url(r'^api2/', include('pressure.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inbox/', include(notifications.urls)),
]
