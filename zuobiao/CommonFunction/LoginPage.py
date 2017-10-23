#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class LoginPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位浮层页立即体验
    def fuceng(self):
        try:
            __fuceng=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/skip_btn")
        except Exception as err:
            assert False,\
            "定位浮层失败"
        return __fuceng
    #定位账号框
    def zhanghao(self):
        try:
            __zhanghao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/account_et")
        except Exception as err:
            assert False, \
                "定位账号框错误"
        return  __zhanghao
    #定位密码框
    def password(self):
        try:
            __password=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/password_et")
        except Exception as err:
            assert False, \
                "定位密码框失败"
        return __password
    #定位忘记密码按钮
    def passbtn(self):
        try:
            __passbtn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/forgot_password_tv")
        except Exception as err:
            assert False, \
                "定位忘记密码是失败"
        return __passbtn
    #定位可显示密码小眼睛
    def eye(self):
        try:
            __eye=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/password_visible_iv")
        except Exception as err:
            assert False, \
                "定位显示密码小眼睛失败"
        return __eye
    #定位登录按钮
    def login_btn(self):
        try:
            __login_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/login_btn")
        except Exception as err:
            assert False, \
                "定位登录按钮失败"
        return __login_btn
    #定位立即注册
    def re_btn(self):
        try:
            __re_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/register_now_tv")
        except Exception as err:
            assert False,\
            "定位立即注册失败"
        return __re_btn

    #定位关闭新手指导按钮
    def close_xin(self):
        try:
            __close_xin=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/guide_close_tv")
        except Exception as err:
            assert False,\
            "关闭新手指导失败"
        return __close_xin

