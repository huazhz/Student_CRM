# from django.forms import Form,ModelForm
# from extra_apps.crm import models
# #Form == >可以自己混合各个字段在里面做验证
# #ModelForm  ==> 可以直接把一张表里的数据变成一张form
#
#
# class CustomerModelForm(ModelForm):
#     class Meta:
#         model = models.Customer
#         exclude = ()
#         '''加样式'''
#     def __init__(self,*args,**kwargs):
#         '''重写初始化方法'''
#         super(CustomerModelForm,self).__init__(*args,**kwargs)
#         #self.fields['qq'].widget.attrs['class'] = "form-control"  #这样给一个字段加了样式，注意如歌多个字段的话肯定是不现实的，所以见下面用for循环实现
#         for field_name in self.base_fields:
#             field = self.base_fields[field_name]
#             field.widget.attrs.update({'class':'form-control'})
