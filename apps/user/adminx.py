#!/usr/bin/env python
# encoding: utf-8

__author__ = 'mxrain'
__date__ = "2018/9/26 15:22"

import xadmin
from .models import EmailVerifyRecord,Banner


class EmailVerifyRecordAdmin(object):
    list_display= ["code","email","send_type","send_time"]
    search_fields = ['code',"email","send_type"]
    list_filter = ["code","email","send_type","send_time"]


class BannerAdmin(object):
    list_display = ["title", "url", "add_time"]
    search_fields = ["title", "url"]
    list_filter = ["title", "url", "add_time","image","index"]


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)