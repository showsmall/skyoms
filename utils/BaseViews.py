# -*- coding:utf-8 -*-

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class ReturnFormatMixin(object):

    @classmethod
    def get_ret(cls):
        return {'status': 0, 'msg': '', 'data': {}}


class DefaultPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 10
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'page_size'

    # 获取URL参数中传入的页码key
    page_query_param = 'page'

    # 最大支持的每页显示的数据条数
    max_page_size = 500

class BaseView(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    # 分页
    pagination_class = DefaultPagination
    # 搜索
    search_fields = ()  # 用于单一搜索：接收前端的search参数，从多个字段中匹配，或的关系
    #filter_class = None  # 用于综合搜索：可接收前端的多个查询参数，对相应的字段匹配，且的关系