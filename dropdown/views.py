from django.shortcuts import render
from django.apps import apps
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

class dropdownOption(GenericAPIView):
    serializer_class = dropdownOptionSerializers
    def get(self, request, table, format=None, *args, **kwargs):
        print('table', table)
        model = apps.get_model('dropdown', table)
        data = list(model.objects.values())
        serializer = dropdownOptionSerializers(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        res = Response()
        res.status_code = status.HTTP_200_OK
        res.data = {'option': serializer.data}
        return res