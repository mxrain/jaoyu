from datetime import datetime

from django.db import models

# Create your models here.


# 城市
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"详细地址")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# -课程机构
class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("pxjg", u"培训机构"),
        ("gx", u"高校"),
        ("gr", u"个人"),
    )
    name = models.CharField(max_length=50, verbose_name=u"机构名字")
    desc = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name=u"机构类别", default="pxjg")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"封面图片")
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    students = models.IntegerField(default=0,verbose_name="学习人数")
    course_nums = models.IntegerField(default=0,verbose_name="课程数")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 教师
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构",on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"教师名字")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(default='',upload_to="teacher/%Y/%m",verbose_name="头像",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
