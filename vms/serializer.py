# -*- coding:utf-8 -*-


from rest_framework import  serializers
from .models import DataStores,DataCenters,VirtualHosts,Dedicatedhosts,Clusters,NetworkAdapters


class DataCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCenters
        fields = '__all__'
class ClustersSerializer(serializers.ModelSerializer):
    datacenter = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Clusters
        fields = '__all__'
        #depth = 2
class DataStoresSerializer(serializers.ModelSerializer):
    datacenter = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = DataStores
        fields = '__all__'

class NetworkAdaptersSerializer(serializers.ModelSerializer):
    datacenter = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = NetworkAdapters
        fields = '__all__'

class DedicatedhostsSerializer(serializers.ModelSerializer):
    datacenter = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    cluster= serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    datastore= serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    network= serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Dedicatedhosts
        fields = '__all__'
class VirtualHostsSerializer(serializers.ModelSerializer):
    datacenter = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    network = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = VirtualHosts
        fields = '__all__'


