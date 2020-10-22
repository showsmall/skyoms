
from rest_framework import serializers
from users.models import UserMenu, UserRouter, UserProfile
from vms.models import DataCenters, Clusters, DataStores, NetworkAdapters, Dedicatedhosts, VirtualHosts
from assets.models import IDC, Hosts, HostGroup

    

class UserMenuSerializer(serializers.ModelSerializer):
    parent_text = serializers.CharField(source="parent.name", read_only=True)
    permission_text = serializers.CharField(source="permission.name", read_only=True)

    class Meta:
        model = UserMenu
        fields = "__all__"
        

class UserRouterSerializer(serializers.ModelSerializer):
    permission_text = serializers.CharField(source="permission.name", read_only=True)

    class Meta:
        model = UserRouter
        fields = "__all__"
        

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = "__all__"
        

class DataCentersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DataCenters
        fields = "__all__"
        

class ClustersSerializer(serializers.ModelSerializer):
    datacenter_text = serializers.CharField(source="datacenter.name", read_only=True)

    class Meta:
        model = Clusters
        fields = "__all__"
        

class DataStoresSerializer(serializers.ModelSerializer):
    datacenter_text = serializers.CharField(source="datacenter.name", read_only=True)

    class Meta:
        model = DataStores
        fields = "__all__"
        

class NetworkAdaptersSerializer(serializers.ModelSerializer):
    datacenter_text = serializers.CharField(source="datacenter.name", read_only=True)

    class Meta:
        model = NetworkAdapters
        fields = "__all__"
        

class DedicatedhostsSerializer(serializers.ModelSerializer):
    cluster_text = serializers.CharField(source="cluster.name", read_only=True)
    datacenter_text = serializers.CharField(source="datacenter.name", read_only=True)

    class Meta:
        model = Dedicatedhosts
        fields = "__all__"
        

class VirtualHostsSerializer(serializers.ModelSerializer):
    datacenter_text = serializers.CharField(source="datacenter.name", read_only=True)

    class Meta:
        model = VirtualHosts
        fields = "__all__"
        

class IDCSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IDC
        fields = "__all__"
        

class HostsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hosts
        fields = "__all__"
        

class HostGroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HostGroup
        fields = "__all__"
        