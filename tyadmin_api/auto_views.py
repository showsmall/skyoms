
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from users.models import UserMenu, UserRouter, UserProfile
from vms.models import DataCenters, Clusters, DataStores, NetworkAdapters, Dedicatedhosts, VirtualHosts
from assets.models import IDC, Hosts, HostGroup

from tyadmin_api.auto_serializers import UserMenuSerializer, UserRouterSerializer, UserProfileSerializer, DataCentersSerializer, ClustersSerializer, DataStoresSerializer, NetworkAdaptersSerializer, DedicatedhostsSerializer, VirtualHostsSerializer, IDCSerializer, HostsSerializer, HostGroupSerializer
from tyadmin_api.auto_filters import UserMenuFilter, UserRouterFilter, UserProfileFilter, DataCentersFilter, ClustersFilter, DataStoresFilter, NetworkAdaptersFilter, DedicatedhostsFilter, VirtualHostsFilter, IDCFilter, HostsFilter, HostGroupFilter
    
    
class UserMenuViewSet(XadminViewSet):
        serializer_class = UserMenuSerializer
        queryset = UserMenu.objects.all()
        filter_class = UserMenuFilter
        search_fields = ["path","title","icon"]
        
    
class UserRouterViewSet(XadminViewSet):
        serializer_class = UserRouterSerializer
        queryset = UserRouter.objects.all()
        filter_class = UserRouterFilter
        search_fields = ["path","name","title","component"]
        
    
class UserProfileViewSet(XadminViewSet):
        serializer_class = UserProfileSerializer
        queryset = UserProfile.objects.all()
        filter_class = UserProfileFilter
        search_fields = ["password","username","first_name","last_name","email","mobile","name"]
        
    
class DataCentersViewSet(XadminViewSet):
        serializer_class = DataCentersSerializer
        queryset = DataCenters.objects.all()
        filter_class = DataCentersFilter
        search_fields = ["name","cputotal","cpuusage","memtotal","memusage","datatotal","datafree"]
        
    
class ClustersViewSet(XadminViewSet):
        serializer_class = ClustersSerializer
        queryset = Clusters.objects.all()
        filter_class = ClustersFilter
        search_fields = ["name","cputotal","cpuusage","memtotal","memusage","datatotal","datafree"]
        
    
class DataStoresViewSet(XadminViewSet):
        serializer_class = DataStoresSerializer
        queryset = DataStores.objects.all()
        filter_class = DataStoresFilter
        search_fields = ["name","capacity","freespace"]
        
    
class NetworkAdaptersViewSet(XadminViewSet):
        serializer_class = NetworkAdaptersSerializer
        queryset = NetworkAdapters.objects.all()
        filter_class = NetworkAdaptersFilter
        search_fields = ["name","vlanid","type"]
        
    
class DedicatedhostsViewSet(XadminViewSet):
        serializer_class = DedicatedhostsSerializer
        queryset = Dedicatedhosts.objects.all()
        filter_class = DedicatedhostsFilter
        search_fields = ["name","conState","powerState","uuid","cpumodel","cputotal","cpuusage","memtotal","memusage"]
        
    
class VirtualHostsViewSet(XadminViewSet):
        serializer_class = VirtualHostsSerializer
        queryset = VirtualHosts.objects.all()
        filter_class = VirtualHostsFilter
        search_fields = ["name","ip","conState","powerState","memtotal","os","cpuusage","memusage","store_usage"]
        
    
class IDCViewSet(XadminViewSet):
        serializer_class = IDCSerializer
        queryset = IDC.objects.all()
        filter_class = IDCFilter
        search_fields = ["name"]
        
    
class HostsViewSet(XadminViewSet):
        serializer_class = HostsSerializer
        queryset = Hosts.objects.all()
        filter_class = HostsFilter
        search_fields = ["hostname","server_type","status","cpu_info","os","os_kernel","memory","disk","desc"]
        
    
class HostGroupViewSet(XadminViewSet):
        serializer_class = HostGroupSerializer
        queryset = HostGroup.objects.all()
        filter_class = HostGroupFilter
        search_fields = ["name"]
        