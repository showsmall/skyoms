from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.text import slugify
import uuid
import random
import string
# Create your models here.


class IDC(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name=u'机房', error_messages={'unique': '该机房已存在，请不要重复添加'})
    servers = models.ManyToManyField('Hosts')
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'idc'
        verbose_name = u"机房"
        verbose_name_plural = verbose_name

class Hosts(models.Model):
    ASSET_STATUS = (
        ('online','上线'),
        ('offline','下线')
    )
    ASSET_TYPE = (
        ('physical','物理机'),
        ('virtual','虚拟机'),

    )
    ip = models.GenericIPAddressField(verbose_name='IP',unique=True,error_messages={'blank':u'IP地址不能为空','unique':u'该地址已存在，请不要重复添加'})
    hostname = models.CharField(max_length=32,verbose_name=u'主机名',unique=True,error_messages={'unique':u'该名称已存在，请不要重复添加'})
    server_type = models.CharField(choices=ASSET_TYPE,default='virtual',max_length=10,verbose_name=u'服务器类型')
    status = models.CharField(choices=ASSET_STATUS,default='offline',verbose_name=u'状态',max_length=10)
    cpu_info = models.CharField(max_length=128, verbose_name='CPU', blank=True, null=True)
    os = models.CharField(max_length=64, blank=True, null=True, verbose_name='系统')
    os_kernel = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'系统内核')
    memory = models.CharField(max_length=12, verbose_name=u'内存/G', blank=True, null=True)
    disk = models.CharField(max_length=12, verbose_name=u'硬盘/G', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    desc = models.CharField(max_length=200, verbose_name=u'描述', blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'hosts'
        verbose_name = u'主机'
        verbose_name_plural = verbose_name

class HostGroup(models.Model):
    name = models.CharField(max_length=32,verbose_name=u'主机组名',unique=True)
    host = models.ManyToManyField('Hosts')
    ctime = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'hostgroup'
        verbose_name = u'主机组'
        verbose_name_plural = verbose_name