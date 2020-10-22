# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyoms.settings")
django.setup()

from celery import  Celery
from skyoms import settings

# 使用redis作为消息队列，backend也默认为broker使用的队列服务
app = Celery('skyoms',broker=settings.REDIS_HOST)
# 载入django配置文件中以 CELERY 开头的配置
app.config_from_object('skyoms.settings',namespace='CELERY')

# 自动发现每个app下的tasks文件
app.autodiscover_tasks()