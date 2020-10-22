
from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from users.models import UserMenu, UserRouter, UserProfile
from vms.models import DataCenters, Clusters, DataStores, NetworkAdapters, Dedicatedhosts, VirtualHosts
from assets.models import IDC, Hosts, HostGroup

        

class UserMenuFilter(filters.FilterSet):
    parent_text = filters.CharFilter(field_name="parent")
    permission_text = filters.CharFilter(field_name="permission")

    class Meta:
        model = UserMenu
        exclude = []
    

class UserRouterFilter(filters.FilterSet):
    permission_text = filters.CharFilter(field_name="permission")

    class Meta:
        model = UserRouter
        exclude = []
    

class UserProfileFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = UserProfile
        exclude = ["image","image"]
    

class DataCentersFilter(filters.FilterSet):
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = DataCenters
        exclude = []
    

class ClustersFilter(filters.FilterSet):
    datacenter_text = filters.CharFilter(field_name="datacenter")
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = Clusters
        exclude = []
    

class DataStoresFilter(filters.FilterSet):
    datacenter_text = filters.CharFilter(field_name="datacenter")
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = DataStores
        exclude = []
    

class NetworkAdaptersFilter(filters.FilterSet):
    datacenter_text = filters.CharFilter(field_name="datacenter")
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = NetworkAdapters
        exclude = []
    

class DedicatedhostsFilter(filters.FilterSet):
    cluster_text = filters.CharFilter(field_name="cluster")
    datacenter_text = filters.CharFilter(field_name="datacenter")
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = Dedicatedhosts
        exclude = []
    

class VirtualHostsFilter(filters.FilterSet):
    datacenter_text = filters.CharFilter(field_name="datacenter")
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = VirtualHosts
        exclude = []
    

class IDCFilter(filters.FilterSet):
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = IDC
        exclude = []
    

class HostsFilter(filters.FilterSet):
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = Hosts
        exclude = []
    

class HostGroupFilter(filters.FilterSet):
    ctime = DateFromToRangeFilter(field_name="ctime")
    utime = DateFromToRangeFilter(field_name="utime")

    class Meta:
        model = HostGroup
        exclude = []
    