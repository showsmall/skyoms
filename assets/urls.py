# -*- coding:utf-8 -*-
from rest_framework.routers import DefaultRouter
from assets.views import HostGroupViewSet,HostViewSet,IDCViewSet


router = DefaultRouter()



router.register(r'idc',IDCViewSet,basename="idc")
router.register(r'host',HostViewSet,basename="host")
router.register(r'hostgroup',HostGroupViewSet,basename="hostgroup")

urlpatterns = []
urlpatterns += router.urls