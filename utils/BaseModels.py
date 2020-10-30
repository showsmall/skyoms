# -*- coding:utf-8 -*-


from django.db import models
from datetime import  datetime


class BaseModel(models.Model):
    '''

    基础model
    '''
    desc = models.TextField(verbose_name=u'描述', blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    class Meta:
        abstract = True
