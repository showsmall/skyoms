# DRF+VUE前后端分离项目
使用Coreapi展示api-doc  
ElementUI展示前端页面UI  
数据库采用mysql 和Redis



# celery定时任务

1.启动celery
```
celery -A skyoms worker -l debug
```  

2.启动celery-beat  
```
celery -A skyoms beat -l info
``` 