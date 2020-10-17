from django.contrib import admin
from .models import DataCenters,Clusters,DataStores,NetworkAdapters,Dedicatedhosts,VirtualHosts

# Register your models here.



class DataCentersAdmin(admin.ModelAdmin):
    model = DataCenters

class ClustersAdmin(admin.ModelAdmin):
    model = Clusters

class DataStoresAdmin(admin.ModelAdmin):
    model = DataStores

class NetworkAdaptersAdmin(admin.ModelAdmin):
    model = NetworkAdapters
class DedicatedhostsAdmin(admin.ModelAdmin):
    model = Dedicatedhosts

class VirtualHostsAdmin(admin.ModelAdmin):
    model = VirtualHosts

#在admin中注册绑定

admin.site.register(DataCenters, DataCentersAdmin)
admin.site.register(Clusters,ClustersAdmin)
admin.site.register(DataStores,DataStoresAdmin)
admin.site.register(NetworkAdapters,NetworkAdaptersAdmin)
admin.site.register(Dedicatedhosts,DedicatedhostsAdmin)
admin.site.register(VirtualHosts,VirtualHostsAdmin)

