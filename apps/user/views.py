from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password # 加密密码工具
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from user.forms import LoginForms, RegisterForms, ForgetpwdForms, ModifyPwdForm
from user.models import UserProfile, EmailVerifyRecord
# Create your views here.

# 自定义验证用户名/邮箱/密码的类
from utils.email_send import send_register_eamil


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(password=password))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 设置登录验证views
class LoginViews(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        login_forms = LoginForms(request.POST)
        if login_forms.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html",{})
                else:
                    return render(request, "login.html", {"msg":"帐号未激活"})
            else:
                return render(request, "login.html", {"msg":"账号密码有误"})
        else:
            return render(request, "login.html",{"login_forms":login_forms})


# 注册view
class RegisterViews(View):
    # get请求时直接带 验证码显示
    def get(self,request):
        register_form = RegisterForms()
        return render(request, 'register.html',{"register_form":register_form})

    # post注册时对 username和password处理
    def post(self, request):
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            # 实例化一个user_profile对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False # 用户未激活
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_eamil(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


# 激活用户
class ActiveUserView(View):

    def get(self,request,active_code):
        all_record = EmailVerifyRecord.objects.filter(code = active_code)
        if all_record:
            for record in all_record:
                # 如果验证码使用过
                if record.used:
                    return render(request,"active_fail.html")
                else:
                    email = record.email
                    user = UserProfile.objects.get(email=email)
                    user.is_active = True
                    user.save()
            all_record.update(used=True)
        else:
            return render(request,"active_fail.html")

        return render(request, "login.html")


# 找回密码页面get 和post的view
class ForgetpawView(View):
    def get(self,request):
        forgetpwd_forms = ForgetpwdForms()
        return render(request,"forgetpwd.html",{"forgetpwd_forms":forgetpwd_forms})

    def post(self,request):
        forgetpwd_form = ForgetpwdForms(request.POST)
        if forgetpwd_form.is_valid():
            user_name = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(email=user_name):
                send_register_eamil(user_name,"forget",)
                return render(request,"login.html")
            else:
                return render(request,"forgetpwd.html",{"msg":"此邮箱没注册"})
        else:
            return render(request,"forgetpwd.html",{"forgetpwd_form":forgetpwd_form})
        pass


# 找回密码连接get 验证和跳转修改密码页面
class NewpwdView(View):
    def get(self,request,forget_code):
        all_record = EmailVerifyRecord.objects.filter(code=forget_code)
        if all_record:
            for record in all_record:
                if record.used:
                    return render(request, "active_fail.html")
                else:
                    email = record.email
                # 吧邮箱带到下个页面的request
            all_record.update(used=True)
            return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


# 修改新密码的页面post和get
class ModifyPwdView(View):
    '''修改用户密码'''
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致！"})
            user = UserProfile.objects.get(email=email)
            if user:
                user.password = make_password(pwd2)
                user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form })

