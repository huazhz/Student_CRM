import xadmin
from xadmin import views

from .models import UserProfile,School,Customer,Course,ClassList,ConsultRecord,StudyRecord,CourseRecord

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

class CustomerAdmin(object):
    list_display = ['qq','name','phone','stu_id','source','referral_from','course','class_type','customer_note','status','consultant','date','class_list']
    search_fields = ['qq','name','phone','stu_id','source','referral_from','course','class_type','customer_note','status','consultant','date','class_list']
    list_fields = ['qq','name','phone','stu_id','source','referral_from','course','class_type','customer_note','status','consultant','date','class_list']

class SchoolAdmin(object):
    list_display = ['name', 'addr', 'staffs']
    search_fields = ['name', 'addr', 'staffs']
    list_fields = ['name', 'addr', 'staffs']

class CourseAdmin(object):
    list_display = ['name', 'price', 'online_price','online_price']
    search_fields = ['name', 'price', 'online_price','online_price']
    list_fields = ['name', 'price', 'online_price','online_price']

class ClassListAdmin(object):
    list_display = ['course', 'course_type', 'semester', 'start_date','graduate_date','teachers']
    search_fields = ['course', 'course_type', 'semester', 'start_date','graduate_date','teachers']
    list_fields = ['course', 'course_type', 'semester', 'start_date', 'graduate_date', 'teachers']

class ConsultRecordAdmin(object):
    list_display = ['customer','note','status','consultant','date']
    search_fields = ['customer','note','status','consultant','date']
    list_fields = ['customer','note','status','consultant','date']


class StudyRecordAdmin(object):
    list_display = ['course_record','student','record','score','date','note']
    search_fields = ['course_record','student','record','score','date','note']
    list_fields = ['course_record','student','record','score','date','note']


class CourseRecordAdmin(object):
    list_display = ['course','day_num','date','teacher']
    search_fields = ['course','day_num','date','teacher']
    list_fields = ['course','day_num','date','teacher']

xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Customer,CustomerAdmin)
xadmin.site.register(ConsultRecord,ConsultRecordAdmin)
xadmin.site.register(CourseRecord,CourseRecordAdmin)
xadmin.site.register(StudyRecord,StudyRecordAdmin)
xadmin.site.register(School,SchoolAdmin)
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(ClassList,ClassListAdmin)
xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)

