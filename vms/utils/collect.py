# -*- coding:utf-8 -*-
from .vmapi import VcenterApi
from vms.models import *

VC1 = VcenterApi(host='',user='',pwd='')

import time


def CollectDatacenterinfo(vcname):
    print('开始采集Datacenterinfo' + time.strftime('%Y年%m月%d日 %X'))
    response_data = vcname.get_datacenter_list()
    for k,v in response_data:
        try:
            name = v['name']
            numshosts = v['numshosts']
            cputotal = v['cputotal']
            cpuusage = v['cpuusage']
            memtotal = v['memtotal']
            memusage = v['memusage']
            datatotal = v['datatotal']
            datafree = v['datafree']
            numcpuscores = v['numcpuscores']
            vmscount = v['vmscount']
        except Exception as e:
            print(e)
        else:
            update_values = {'name': name,'numshosts': numshosts, 'cputotal': cputotal,
                             'cpuusage': cpuusage, 'memusage': memusage, 'memtotal': memtotal,
                             'datatotal': datatotal, 'datafree': datafree, 'vmscount': vmscount,
                             'numcpuscores':numcpuscores}
            DataCenters.objects.update_or_create(name=name,defaults=update_values)


def CollectClusterinfo(vcname):
    print('开始采集Clusterinfo'+time.strftime('%Y年%m月%d日 %X'))
    response_data = vcname.get_cluster_list()
    for k,v in  response_data:
        try:
            name = v['name']
            datacenter =DataCenters.objects.get(name=v['datacenter'])
            numshosts = v['numshosts']
            cputotal = v['cputotal']
            cpuusage = v['cpuusage']
            memtotal = v['memtotal']
            memusage = v['memusage']
            datatotal = v['datatotal']
            datafree = v['datafree']
            vmscount = v['vmscount']
        except Exception as e:
            print(e)
        else:
            update_values = {'name':name,'datacenter':datacenter,'numshosts':numshosts,'cputotal':cputotal,
                             'cpuusage':cpuusage,'memusage':memusage,'memtotal':memtotal,
                             'datatotal':datatotal,'datafree':datafree,'vmscount':vmscount}
            Clusters.objects.update_or_create(name=name,defaults=update_values)



