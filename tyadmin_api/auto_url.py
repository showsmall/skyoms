from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('user_menu/?', auto_views.UserMenuViewSet)
    
router.register('user_router/?', auto_views.UserRouterViewSet)
    
router.register('user_profile/?', auto_views.UserProfileViewSet)
    
router.register('data_centers/?', auto_views.DataCentersViewSet)
    
router.register('clusters/?', auto_views.ClustersViewSet)
    
router.register('data_stores/?', auto_views.DataStoresViewSet)
    
router.register('network_adapters/?', auto_views.NetworkAdaptersViewSet)
    
router.register('dedicatedhosts/?', auto_views.DedicatedhostsViewSet)
    
router.register('virtual_hosts/?', auto_views.VirtualHostsViewSet)
    
router.register('i_d_c/?', auto_views.IDCViewSet)
    
router.register('hosts/?', auto_views.HostsViewSet)
    
router.register('host_group/?', auto_views.HostGroupViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    