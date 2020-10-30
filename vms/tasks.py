# -*- coding:utf-8 -*-
from __future__ import absolute_import
from skyoms import celery_app
import time
from vms.models import *

from vms.utils.vmapi import VcenterApi



@celery_app.task
def CollectDatacenterinfo(host,user,pwd):
    print('开始采集Datacenterinfo' + time.strftime('%Y年%m月%d日 %X'))
    Vc=VcenterApi(host=host,user=user,pwd=pwd)
    v = Vc.get_datacenter_list()
    name = v['datacentername']
    numhosts = v['numhosts']
    cputotal = v['cputotal']
    cpuusage = v['cpuusage']
    memtotal = v['memtotal']
    memusage = v['memusage']
    datatotal = v['totaldatastore']
    datafree = v['datastorefree']
    numcpuscores = v['numcpucores']
    vmscount = v['vmcount']
    update_values = {'name': name,'numhosts': numhosts, 'cputotal': cputotal,
                             'cpuusage': cpuusage, 'memusage': memusage, 'memtotal': memtotal,
                             'datatotal': datatotal, 'datafree': datafree, 'vmscount': vmscount,
                             'numcpuscores':numcpuscores}
    DataCenters.objects.update_or_create(name=name,defaults=update_values)
    return "Datacenter数据采集成功"

@celery_app.task
def CollectClusterinfo(host,user,pwd):
    print('开始采集Clusterinfo' + time.strftime('%Y年%m月%d日 %X'))
    Vc=VcenterApi(host=host,user=user,pwd=pwd)
    res = Vc.get_cluster_list()
    for item in res:
        name = item.get('clustername')
        numshosts = item.get('numhosts')
        cputotal = item.get('cputotal')
        cpuusage = item.get('cpuusage')
        memtotal = item.get('memtotal')
        memusage = item.get('memusage')
        overallstatus = item.get('overallstatus')
        datatotal = item.get('totaldatastore')
        datafree = item.get('datastorefree')
        vmscount = item.get('vmcount')
        datacentername = item.get('datacentername')
        datacenter = DataCenters.objects.get(name=datacentername)
        update_values = {'name': name,'numshosts': numshosts, 'cputotal': cputotal,'overallstatus':overallstatus,
                             'cpuusage': cpuusage, 'memusage': memusage, 'memtotal': memtotal,
                             'datatotal': datatotal, 'datafree': datafree, 'vmscount': vmscount,
                             'datacenter':datacenter}
        Clusters.objects.update_or_create(name=name,defaults=update_values)
    return "Cluster数据采集成功"

@celery_app.task
def CollectDatastoreinfo(host,user,pwd):
    print('开始采集DataStoreinfo' + time.strftime('%Y年%m月%d日 %X'))
    Vc=VcenterApi(host=host,user=user,pwd=pwd)
    res = Vc.get_datastore_list()
    for item in res:
        name = item.get('name')
        capacity = item.get('capacity')
        freespace = item.get('freespace')
        datacentername = item.get('datacentername')
        datacenter = DataCenters.objects.get(name=datacentername)
        update_values = {'name': name, 'capacity': capacity, 'freespace': freespace,
                             'datacenter':datacenter}
        DataStores.objects.update_or_create(name=name,defaults=update_values)
    return "Datastore数据采集成功"

@celery_app.task
def CollectNetworkinfo(host,user,pwd):
    print('开始采集Networkinfo' + time.strftime('%Y年%m月%d日 %X'))
    Vc=VcenterApi(host=host,user=user,pwd=pwd)
    res = Vc.get_networkport_group_list()
    for item in res:
        name = item.get('name')
        vlanid = item.get('vlanid')
        type = item.get('type')
        datacentername = item.get('datacentername')
        datacenter = DataCenters.objects.get(name=datacentername)
        update_values = {'name': name, 'vlanid': vlanid, 'type': type,
                             'datacenter':datacenter}
        NetworkAdapters.objects.update_or_create(name=name,defaults=update_values)
    return "Network数据采集成功"