from django.shortcuts import render
from rest_framework import viewsets,mixins,generics
from .models import HostGroup,Hosts,IDC
from .serializer import HostGroupSerializer,HostSerializer,IDCSerializer
from vms.views import DefaultPagination
# Create your views here.


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all().order_by("-ctime")
    serializer_class = IDCSerializer
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')


class HostGroupViewSet(viewsets.ModelViewSet):
    queryset = HostGroup.objects.all().order_by("-ctime")
    serializer_class = HostGroupSerializer
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')

class HostViewSet(viewsets.ModelViewSet):
    queryset = Hosts.objects.all().order_by("-ctime")
    serializer_class = HostSerializer
    pagination_class = DefaultPagination
    filter_fields = ['hostname','status','ip']
    search_fields = ('hostname','ip')
    ordering_fields = ('ctime','ip')



