from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import rest_framework as filters

from .models import Bahan
from .serialiezer import *

class DashboardView(
    generics.ListAPIView,
    generics.GenericAPIView,
    mixins.RetrieveModelMixin
    ):
    
    fields = []
    for i in range(1,8):
        fields.append(f'bahan_{i}__nama_bahan')
    
    queryset = Obat.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ObatSerializer
    filter_backends = [SearchFilter]
    search_fields = fields
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
        
class BahanView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    
    queryset = Bahan.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BahanSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nama_bahan']
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
