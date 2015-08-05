from django.db.models.query import QuerySet
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from .models import  YFS201Reading
from .models import  HCSR04Reading
from .models import  HCSR04ReadingSerializer
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

        level_reading = HCSR04Reading(
                sensor_reading=request.data['echo'],
                water_tank=wt)

        flow_reading = YFS201Reading(
                sensor_reading=request.data['total_liters'],
                water_tank=wt)

        level_reading.save()
        flow_reading.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCurrentTankLevel(RetrieveAPIView):
    lookup_field = 'water_tank'
    serializer_class = HCSR04ReadingSerializer

    # Copied from Source ...
    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """

        # Modified... no queryset here

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        # Modified... custom queryset
        try:
            obj = HCSR04Reading.objects.filter(
                **filter_kwargs).order_by('timestamp').last()

        except (TypeError, ValueError):
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
