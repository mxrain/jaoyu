#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Course, Video, Lesson, CourseResource

__author__ = 'mxrain'
__date__ = "2018/9/26 15:22"


# 课程Admin
class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "degree","learn_time","strdents","fav_nums","image","click_nums","add_time"]
    search_fields = ["name", "desc", "detail", "degree","strdents","fav_nums","image","click_nums"]
    list_filter = ["name", "desc", "detail", "degree","learn_time","strdents","fav_nums","image","click_nums","add_time"]


# 章节信息Admin
class LessonAdmin(object):
    list_display = ["course","name","add_time"]
    search_fields = ["course","name"]
    list_filter = ["course__name","name","add_time"]


# 视频admin
class VideoAdmin(object):
    list_display = ["course","name","add_time"]
    search_fields = ["course","name"]
    list_filter = ["course__name","name","add_time"]


# 视频资源
class CourseResourceAdmin(object):
    list_display = ["course","name","download","add_time"]
    search_fields = ["course","name","download"]
    list_filter = ["course__name","name","download","add_time"]


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Video,VideoAdmin)
