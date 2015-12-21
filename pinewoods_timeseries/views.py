from django.shortcuts import render

# Create your views here.
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response

class ViewEcho(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        from IPython import embed; embed()
        return Response(status=status.HTTP_204_NO_CONTENT)
