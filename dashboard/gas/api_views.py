from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from pinewoods_timeseries.views import GenericViewCurrentReading
from .serializers import CylinderWeightSerializer

from .models import GasCylinder
from .models import CylinderWeight

from rest_framework.response import Response

class ViewGasEndpoint(APIView):

    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        try:
            channel = request.data['channel']
            gc = GasCylinder.objects.get(pk=channel)

            weight_reading = CylinderWeight(
                    sensor_reading=request.data['weight'],
                    channel=gc)

            weight_reading.save()

        except Exception as e:
            raise

        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCurrentWeight(GenericViewCurrentReading):
    lookup_field = 'channel'
    model_class = CylinderWeight
    serializer_class = CylinderWeightSerializer
