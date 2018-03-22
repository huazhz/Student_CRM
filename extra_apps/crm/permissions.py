#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie
from django.shortcuts import render,redirect
from django.core.urlresolvers import resolve

perm_dic = {
    'view_customer_list': ['customer_list','GET',[]], #列表里的第一个为url，第二个为方法，第三个为自定义参数
    'view_customer_info': ['customer_detail','GET',[]],
    'edit_own_customer_info': ['customer_detail','POST',['test']],
}

def perm_check(*args,**kwargs):
    request = args[0]
    url_resovle_obj = resolve(request.path_info) #返回完整的url,通过resolve直接转成urls.py里的别名
    '''
    In [1]: from django.core.urlresolvers import resolve

    In [2]: resolve("/crm/customers/").url_name
    Out[2]: 'customer_list'
    '''
    current_url_namespace = url_resovle_obj.url_name
    #app_name = url_resovle_obj.app_name #use this name later
    print("url namespace:",current_url_namespace)
    matched_flag = False # find matched perm item默认不匹配
    matched_perm_key = None
    if current_url_namespace is not None:#如果没有设置URL名称空间，则权限不起作用。
        print("find perm...")
        for perm_key in perm_dic:
            perm_val = perm_dic[perm_key]
            if len(perm_val) == 3:#otherwise invalid perm data format
                url_namespace,request_method,request_args = perm_val
                print(url_namespace,current_url_namespace)
                if url_namespace == current_url_namespace: #matched the url
                    if request.method == request_method:#matched request method
                        if not request_args:#if empty , pass
                            matched_flag = True
                            matched_perm_key = perm_key
                            print('mtched...%s'%(matched_perm_key))
                            break #no need looking for  other perms
                        else:
                            for request_arg in request_args: #might has many args
                                request_method_func = getattr(request,request_method) #get or post mostly
                                #print("----->>>",request_method_func.get(request_arg))
                                if request_method_func.get(request_arg) is not None:
                                    matched_flag = True # the arg in set in perm item must be provided in request data
                                else:
                                    matched_flag = False
                                    print("request arg [%s] not matched" % request_arg)
                                    break #no need go further
                            if matched_flag == True: # means passed permission check ,no need check others
                                print("--passed permission check--")
                                matched_perm_key = perm_key
                                break

    else:#permission doesn't work
        return True

    if matched_flag == True:
        #pass permission check
        perm_str = "crm.%s" %(matched_perm_key) #crm.view_customer_list
        if request.user.has_perm(perm_str):
            print("\033[42;1m--------passed permission check----\033[0m")
            return True
        else:
            print("\033[41;1m ----- no permission ----\033[0m")
            print(request.user,perm_str)
            return False
    else:
        print("\033[41;1m ----- no matched permission  ----\033[0m")

#装饰器至少些两层,第一层传入函数自己,第二层如果有参数就*args,**kwargs
def check_permission(func):
    def wrapper(*args,**kwargs):
        print('---开始做权限监测---')
        if perm_check(*args,**kwargs) is not True:  #监测用户传过来的参数是否有权限
            return render(args[0],'crm/403.html')  #args[0] 实际上等于request
        return func(*args,**kwargs)
    return wrapper