import xadmin
from xadmin import views

from .models import UserProfile,School

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Cnjie后台管理系统"
    site_footer = "Cnjie在线"
    menu_style = "accordion"

class UserProfileAdmin(object):
    list_display = ['user', 'name', 'email']
    search_fields = ['user', 'name', 'email']
    list_fields = ['user','name','email']

class SchoolAdmin(object):
    list_display = ['name', 'addr', 'staffs']
    search_fields = ['name', 'addr', 'staffs']
    list_fields = ['name', 'addr', 'staffs']

xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(School,SchoolAdmin)
xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)

