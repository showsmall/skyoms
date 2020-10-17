from rest_framework import viewsets
from django.views import View
from django.http import HttpResponse
from .serializer import DataCentersSerializer,DataStoresSerializer,ClustersSerializer,NetworkAdaptersSerializer,DedicatedhostsSerializer,VirtualHostsSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Dedicatedhosts,VirtualHosts,DataStores,DataCenters,Clusters,NetworkAdapters

class DefaultPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 10
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'page_size'

    # 获取URL参数中传入的页码key
    page_query_param = 'page'

    # 最大支持的每页显示的数据条数
    max_page_size = 500

class DataCentersViewSet(viewsets.ModelViewSet):
    queryset = DataCenters.objects.all().order_by("-ctime")
    serializer_class = DataCentersSerializer
    #pagination_class = DefaultPagination
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')

class ClustersViewSet(viewsets.ModelViewSet):
    queryset = Clusters.objects.all().order_by("-ctime")
    serializer_class = ClustersSerializer
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')


class DataStoresViewSet(viewsets.ModelViewSet):
    queryset = DataStores.objects.all().order_by("-ctime")
    serializer_class = DataStoresSerializer
    pagination_class = DefaultPagination
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')


class NetworkAdaptersViewSet(viewsets.ModelViewSet):
    queryset = NetworkAdapters.objects.all().order_by("-ctime")
    serializer_class = NetworkAdaptersSerializer
    pagination_class = DefaultPagination
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')



class DedicatedhostsViewSet(viewsets.ModelViewSet):
    queryset = Dedicatedhosts.objects.all().order_by("-ctime")
    serializer_class = DedicatedhostsSerializer
    pagination_class = DefaultPagination
    filter_fields = ['name','uuid','powerState']
    search_fields = ('name','uuid')
    ordering_fields = ('ctime','name','uuid')


class VirtualHostsViewSet(viewsets.ModelViewSet):
    queryset = VirtualHosts.objects.all().order_by("-ctime")
    serializer_class = VirtualHostsSerializer
    pagination_class = DefaultPagination
    filter_fields = ['name','ip','powerState','os']
    search_fields = ('name','os')
    ordering_fields = ('ctime','name')

import json
class GetClusterHost(View):
    '''
    列出所有群集中虚拟机和宿主机的数量，前端Dashboard图标展示
    '''
    def get(self,request):
        json_list =[]
        clusters = Clusters.objects.all()
        for c in clusters:
            json_dict ={}
            json_dict["集群"] = c.name
            json_dict["宿主机数量"] = c.numshosts
            json_dict["虚拟机数量"] = c.vmscount
            json_list.append(json_dict)
        return HttpResponse(json.dumps(json_list),content_type='application/json')

