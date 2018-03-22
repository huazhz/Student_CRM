from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage #分页模块
from crm import models,ModelForms
from crm.permissions import check_permission

from django.core.paginator import Paginator
# Create your views here.

@login_required()
def dashboard(request):
    '''
    定义首页函数，如果未登录就不显示，跳转到登录页面
    :param request:
    :return:
    '''
    return render(request,'crm/dashboard.html')


def acc_login(request):
    '''
    登录的定义
    '''
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password'))
        if user is not None:  # 如果这个user返回不为空，则表示认证成功了
            login(request, user)  # 认证通过了并登录
            return HttpResponseRedirect('/crm/')  # 认证成功跳转到首页
        else:
            login_err = "警告:用户名或者密码错误!"  # 认证不成功则将错误汇报到前端
            return render(request, 'login.html', {'login_err': login_err})
    return render(request, 'login.html')


def acc_logout(request):
    '''
    点击退出后直接到达登录页
    :param request:
    :return:
    '''
    logout(request)
    return HttpResponseRedirect('/accounts/login/') #退出后还是跳转到首页

@check_permission
def customers(request):
    customer_list = models.Customer.objects.all()
    pageinator = Paginator(customer_list, 1)
    page = request.GET.get('page')
    try:
        customer_objs = pageinator.page(page)  # pageinator.page获取具体哪一页，参数page表示前端传过来的参数
    except PageNotAnInteger:  # 判断输入的页数代码不是数字则返回第一页
        customer_objs = pageinator.page(1)
    except EmptyPage:  # 判断输入的页数是否超出范围，超出就直接返回最后一页
        customer_objs = pageinator.page(pageinator.num_pages)
    return render(request, 'crm/customers.html', {'customer_list': customer_objs})

@check_permission
def customers_detail(request,customer_id):
    '''获取客户详情和编辑都通过此视图,customer_id为前端传入，根据该id去获取相关信息'''
    customer_obj = models.Customer.objects.get(id=customer_id)  #返回给前端
    if request.method == "POST": #判断前端请求
        form = ModelForms.CustomerModelForm(request.POST,instance=customer_obj)
        if form.is_valid():
            form.save()
            base_url = "/".join(request.path.split("/")[:-2])
            return redirect(base_url)
    else:
        form = ModelForms.CustomerModelForm(instance=customer_obj) #将获取到的后短信洗在前端展示
    return render(request,'crm/customers_detail.html',{'customer_forms':form})




