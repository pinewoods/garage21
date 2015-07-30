from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from .models import  Reading
from .models import  SensorType
from .models import  WaterTank

class ViewReadings(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)

    def post(self, request, format=None):
        """
        Recives data from sensors.
        """
        wt = WaterTank.objects.get(pk=1)

        level_reading = Reading(
                sensor_reading=request.data['echo'],
                sensor_type=SensorType.objects.get(pk=1),
                water_tank=wt)

        flow_reading = Reading(
                sensor_reading=request.data['total_liters'],
                sensor_type=SensorType.objects.get(pk=2),
                water_tank=wt)

        level_reading.save()
        flow_reading.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

