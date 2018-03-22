#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie

from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def zhu_upper(value):
    print("val from template-tags:", value)
    return value.upper()

@register.simple_tag
def guess_page(current_page,loop_num):
    '''在前端做判断只去当前页前后指定多少页'''
    offset = abs(current_page - loop_num)
    #接收两个参数并算出一个结果offset其实就是一个绝对值 
    if offset < 3: #这个值可以自定义 
        '''如果小于3则执行下面操作'''
        if current_page == loop_num: #页面相等时则是当前页就会active 
            page_ele = '''<li class="active"><a href="?page=%s">%s</a></li>'''%(loop_num,loop_num)
        else:
            page_ele = '''<li class=""><a href="?page=%s">%s</a></li>'''%(loop_num,loop_num)
        return format_html(page_ele) #强制变成html页码 
    else:
        return ''
