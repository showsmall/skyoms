# -*- coding:utf-8 -*-
from rest_framework import  serializers
from .models import HostGroup,Hosts,IDC

class HostGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostGroup
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosts
        fields = '__all__'

class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = '__all__'