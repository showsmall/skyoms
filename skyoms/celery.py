# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os
from celery import  Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyoms.settings")

app = Celery('skyoms',
             broker='redis://:Redis@123@127.0.0.1:6379/1',
             backend='redis://:Redis@123@127.0.0.1:6379/3')
# 载入django配置文件中以 CELERY 开头的配置
app.config_from_object('skyoms.settings',namespace='CELERY')

# 自动发现每个app下的tasks文件
app.autodiscover_tasks()
