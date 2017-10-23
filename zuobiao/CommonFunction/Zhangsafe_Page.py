#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Zhangsage_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #绑定手机号
    def Bind_mobile(self):
        try:
            __Bind_mobile=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/bind_mobile_ll")
        except Exception as err:
            assert False,\
            "定位绑定手机号失败"
        return __Bind_mobile

    #绑定邮箱
    def Bind_email(self):
        try:
            __Bind_email=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/bind_email_ll")
        except Exception as err:
            assert False,\
            "绑定邮箱失败"
        return __Bind_email

    #修改密码
    def Modify_password(self):
        try:
            __Modify_password=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/modify_password_ll")
        except Exception as err:
            assert False,\
            "修改密码失败"
        return __Modify_password

    #修改密码 验证原密码  输入框 输入原始密码
    def Cet_input_your_pwd(self):
        try:
            __Cet_input_your_pwd=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cet_input_your_pwd")
        except Exception as err:
            assert False,\
            "修改密码 验证原密码  输入框 输入原始密码失败"
        return __Cet_input_your_pwd
    #修改密码 验证原密码  输入框 输入原始密码  确定键
    def Btn_confirm(self):
        try:
            __Btn_confirm=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/tv_confirm")
        except Exception as err:
            assert False,\
            "修改密码 验证原密码  输入框 输入原始密码  确定键失败"
        return __Btn_confirm


    #设置新密码
    def Input_new_pwd_cet(self):
        try:
            __Input_new_pwd_cet=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_new_pwd_cet")
        except Exception as err:
            assert False,\
            "设置新密码失败"
        return __Input_new_pwd_cet
   #设置再次输入新密码
    def Input_new_pwd_again_cet(self):
        try:
            __Input_new_pwd_again_cet=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_new_pwd_again_cet")
        except Exception as err:
            assert False,\
            "设置新密码失败"
        return __Input_new_pwd_again_cet

    #定位绑定手机号弹窗取消
    def Item_tv(self):
        try:
            __Item_tv=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False,\
            "点位绑定手机号弹窗取消失败"
        return __Item_tv
