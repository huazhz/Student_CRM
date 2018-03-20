#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie

perm_dic = {
    'view_customer_list': ['customer_list','GET',[]], #列表里的第一个为url，第二个为方法，第三个为自定义参数
    'view_customer_info': ['customer_detail','GET',[]],
    'edit_own_customer_info': ['customer_detail','POST',['test']],
}