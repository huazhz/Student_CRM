#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie

from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.dashboard),
    url(r'^customers/$', views.customers),
    url(r'^customers/(\d+)/$',views.customers_detail),
]
