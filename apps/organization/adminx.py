#!/usr/bin/env python3
# encoding: utf-8
import xadmin
from organization.models import CourseOrg, Teacher, CityDict

__author__ = 'mxrain'
__date__ = "2018/9/26 15:22"


# 城市信息Admin
class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]


# 课程机构基本信息admin
class CourseOrgAdmin(object):
    list_display = ["name","desc","click_nums","fav_nums","address","city","add_time"]
    search_fields = ["name","desc","click_nums","fav_nums","address","city"]
    list_filter = ["name","desc","click_nums","fav_nums","address","city","add_time"]


# 教师基本信息Admin
class TeacherAdmin(object):
    list_display = ["name", "org", "work_years", "work_company", "points", "click_nums", "fav_nums", "add_time"]
    search_fields = ["name", "org", "work_years", "work_company", "points", "click_nums", "fav_nums"]
    list_filter = ["name", "org", "work_years", "work_company", "points", "click_nums", "fav_nums", "add_time"]





xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
