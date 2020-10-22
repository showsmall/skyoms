from django.db import models
from datetime import datetime
# Create your models here.


class DataCenters(models.Model):
    '''数据中心'''
    name = models.CharField(max_length=128,verbose_name=u'数据中心名',unique=True)
    cputotal = models.CharField(max_length=64,verbose_name=u'CPU总计')
    cpuusage = models.CharField(max_length=64,verbose_name=u'CPU使用量')
    memtotal = models.CharField(max_length=64,verbose_name=u'内存总计')
    memusage = models.CharField(max_length=64,verbose_name=u'内存使用量')
    datatotal = models.CharField(max_length=64,verbose_name=u'存储总计')
    datafree  = models.CharField(max_length=64,verbose_name=u'存储剩余量')
    numhosts = models.SmallIntegerField(verbose_name=u'宿主机数量')
    numcpuscores = models.SmallIntegerField(verbose_name=u'CPU总核数')
    vmscount = models.SmallIntegerField(verbose_name=u'虚拟机数量')
    desc = models.TextField(verbose_name=u'描述',blank=True,null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'data_centers'
        verbose_name = u"数据中心"
        verbose_name_plural = verbose_name

class Clusters(models.Model):
    '''集群'''
    name = models.CharField(max_length=128,verbose_name=u'集群名',unique=True)
    datacenter = models.ForeignKey('DataCenters',verbose_name=u'数据中心',on_delete=models.CASCADE)
    numshosts = models.SmallIntegerField(verbose_name=u'宿主机数量')
    cputotal = models.CharField(max_length=64, verbose_name=u'CPU总计')
    cpuusage = models.CharField(max_length=64, verbose_name=u'CPU使用量')
    memtotal = models.CharField(max_length=64, verbose_name=u'内存总计')
    memusage = models.CharField(max_length=64, verbose_name=u'内存使用量')
    datatotal = models.CharField(max_length=64, verbose_name=u'存储总计')
    datafree = models.CharField(max_length=64, verbose_name=u'存储剩余量')
    vmscount = models.SmallIntegerField(verbose_name=u'虚拟机数量')
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'clusters'
        verbose_name = u'集群'
        verbose_name_plural = verbose_name

class DataStores(models.Model):
    '''存储'''
    name = models.CharField(max_length=32,verbose_name=u'存储名')
    datacenter = models.ForeignKey('DataCenters', verbose_name=u"数据中心",on_delete=models.CASCADE)
    capacity = models.CharField(max_length=64,verbose_name=u'存储总量')
    freespace = models.CharField(max_length=64,verbose_name=u'存储剩余')
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'datastores'
        verbose_name = u'存储'
        verbose_name_plural = verbose_name

class NetworkAdapters(models.Model):
    '''网络'''
    name = models.CharField(max_length=64,verbose_name=u'分布式交换机名')
    datacenter = models.ForeignKey('DataCenters', verbose_name=u'数据中心',on_delete=models.CASCADE)
    vlanid = models.CharField(max_length=32,verbose_name=u'VlanID')
    type = models.CharField(max_length=32,verbose_name=u'类型')
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'networkadapters'
        verbose_name = u'网络端口'
        verbose_name_plural = verbose_name

class Dedicatedhosts(models.Model):
    '''宿主机'''
    name = models.CharField(max_length=32,verbose_name=u'主机名',unique=True)
    cluster = models.ForeignKey('Clusters',verbose_name=u'集群',on_delete=models.CASCADE)
    datacenter = models.ForeignKey(DataCenters,verbose_name="数据中心",on_delete=models.CASCADE)
    network = models.ManyToManyField('NetworkAdapters',verbose_name=u'网络')
    datastore = models.ManyToManyField('DataStores',verbose_name=u'存储')
    conState = models.CharField(max_length=32,verbose_name=u'连接状态')
    powerState = models.CharField(max_length=32,verbose_name=u'电源状态')
    uuid = models.CharField(max_length=128,verbose_name=u'UUID')
    cpumodel = models.CharField(max_length=128,verbose_name=u'CPU类型')
    cpunums = models.SmallIntegerField(verbose_name=u'CPU数量')
    cpucores = models.SmallIntegerField(verbose_name=u'CPU核数')
    cputhreads = models.SmallIntegerField(verbose_name=u'CPU线程数')
    cputotal = models.CharField(max_length=64, verbose_name=u'CPU总计')
    cpuusage = models.CharField(max_length=64, verbose_name=u'CPU使用量')
    memtotal = models.CharField(max_length=32,verbose_name=u'总内存')
    memusage = models.CharField(max_length=32,verbose_name=u'内存使用数')
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'dedicatedhosts'
        verbose_name = u'宿主机'
        verbose_name_plural = verbose_name

class VirtualHosts(models.Model):
    '''虚拟机'''
    name = models.CharField(max_length=128,verbose_name=u'虚拟机名称')
    ip = models.CharField(max_length=64,verbose_name=u'宿主机IP')
    datacenter = models.ForeignKey('DataCenters',on_delete=models.CASCADE)
    conState = models.CharField(max_length=32,verbose_name=u'连接状态')
    powerState = models.CharField(max_length=32,verbose_name=u'电源状态')
    cpunums = models.SmallIntegerField(verbose_name=u'CPU数量')
    memtotal = models.CharField(max_length=32,verbose_name=u'总内存')
    network = models.ManyToManyField('NetworkAdapters')
    os = models.CharField(max_length=64,verbose_name=u'系统名称')
    cpuusage = models.CharField(max_length=32,verbose_name=u'CPU使用量')
    memusage = models.CharField(max_length=32,verbose_name=u'内存使用量')
    store_usage = models.CharField(max_length=32,verbose_name=u'存储使用量')
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'virtualhosts'
        verbose_name_plural = u'虚拟机'
        verbose_name = verbose_name_plural
