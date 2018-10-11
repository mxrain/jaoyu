"""jaoyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from jaoyu.settings import MEDIA_ROOT

from user.views import LoginViews, RegisterViews, ActiveUserView, ForgetpawView, NewpwdView, ModifyPwdView

urlpatterns = [
    path('admin/', xadmin.site.urls),  # xadmin页面
    path('', TemplateView.as_view(template_name="index.html"), name="index"),  # 主页
    path('login/', LoginViews.as_view(), name="login"),  # 登录页面
    path('register/', RegisterViews.as_view(), name="register"),  # 注册页面、注册表单post
    path('captcha/', include('captcha.urls')),  # 引用django-captcha自带的urls # 验证码图片
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),  # 注册激活get页面
    path('forget/', ForgetpawView.as_view(), name="forgetpaw"), # 忘记密码页面
    re_path("reset/(?P<forget_code>.*)/", NewpwdView.as_view(), name="newpwd"), # 重置密码跳转连接
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'), # post修改用户密码
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}), # 上传图片下载图片连接
    # 课程机构app相关url配置
    path("org/", include('organization.urls', namespace="org")), # /org/
]
