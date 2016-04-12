from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

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
                    gas_cylinder=gc)

            weight_reading.save()

        except Exception as e:
            raise

        return Response(status=status.HTTP_204_NO_CONTENT)
