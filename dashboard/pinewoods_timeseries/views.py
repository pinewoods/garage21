from django.shortcuts import render

# Create your views here.
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response

class ViewEcho(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        from IPython import embed; embed()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenericViewCurrentReading(RetrieveAPIView):
    lookup_field = None
    serializer_class = None
    model_class = None
    ts_field = 'timestamp'

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
            obj = self.model_class.objects.filter(
                **filter_kwargs).order_by(self.ts_field).last()

        except (TypeError, ValueError):
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
