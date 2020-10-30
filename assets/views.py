from .models import HostGroup,Hosts,IDC
from .serializer import HostGroupSerializer,HostSerializer,IDCSerializer
from utils.BaseViews import BaseView
# Create your views here.


class IDCViewSet(BaseView):
    queryset = IDC.objects.all().order_by("-ctime")
    serializer_class = IDCSerializer
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')


class HostGroupViewSet(BaseView):
    queryset = HostGroup.objects.all().order_by("-ctime")
    serializer_class = HostGroupSerializer
    filter_fields = ['name',]
    search_fields = ('name',)
    ordering_fields = ('ctime','name')

class HostViewSet(BaseView):
    queryset = Hosts.objects.all().order_by("-ctime")
    serializer_class = HostSerializer
    filter_fields = ['hostname','status','ip']
    search_fields = ('hostname','ip')
    ordering_fields = ('ctime','ip')



