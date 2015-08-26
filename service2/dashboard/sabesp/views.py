import datetime
import calendar
import collections
from django.shortcuts import render
from bisect import bisect_left

import pytz

from django.db.models.query import QuerySet
from django.http import Http404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import SabespReading
from .models import SabespReadingSerializer
from .models import SabespProfile
from .models import SabespProfileSerializer

# Create your views here.
class SabespReadingViewSet(viewsets.ModelViewSet):
    queryset = SabespReading.objects.all().order_by('-reading_competence')
    serializer_class = SabespReadingSerializer

class SabesprofileRetrieve(ListAPIView):
    serializer_class = SabespProfileSerializer
        
    def get_queryset(self):
        user = self.request.user
        return SabespProfile.objects.filter(user=user)
