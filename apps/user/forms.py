#!/usr/bin/env python3
# encoding: utf-8

__author__ = 'mxrain'
__date__ = "2018/9/30 23:18"
from django import forms
from captcha.fields import CaptchaField


# 登录表单
class LoginForms(forms.Form):
    '''
    required: 必须要输入
    '''
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5,max_length=16)


# 注册验证表单
class RegisterForms(forms.Form):
    '''
    error_messages: error信息变成中文
    '''
    email = forms.CharField(required=True,error_messages={'required':'邮箱不能为空'})
    password = forms.CharField(required=True, min_length=5, max_length=16,error_messages={'required':'密码不能为空'})
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


# 找回密码输入发送邮箱
class ForgetpwdForms(forms.Form):
    email = forms.CharField(required=True,error_messages={"required":"邮箱不能为空"})
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


#找回密码-输入新密码
class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True, min_length=5,error_messages={'required':'密码不能为空'})
    password2 = forms.CharField(required=True, min_length=5,error_messages={'required':'密码不能为空'})