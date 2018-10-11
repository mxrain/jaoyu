#!/usr/bin/env python
# encoding: utf-8

__author__ = 'mxrain'
__date__ = "2018/9/26 15:22"

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner


# 把全站的setting放在user的xadmin这里
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 右上字,下字,把导航栏缩起来
class GlobalSettings(object):
    site_title = "后台管理系统" # 上字
    site_footer = "在线网" # 下字
    menu_style = "accordion" # 导航栏缩起


# 邮箱验证码后台数据 搜索栏显示setting
class EmailVerifyRecordAdmin(object):
    list_display= ["code","email","send_type","send_time"]
    search_fields = ['code',"email","send_type"]
    list_filter = ["code","email","send_type","send_time"]


class BannerAdmin(object):
    list_display = ["title", "url", "add_time"]
    search_fields = ["title", "url"]
    list_filter = ["title", "url", "add_time","image","index"]


# 显示验证码数据栏
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
# 显示布伦数据栏
xadmin.site.register(Banner,BannerAdmin)
# 显示主题按钮
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 显示全局设置
xadmin.site.register(views.CommAdminView,GlobalSettings)

