#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class MyPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver
    #定位我的页面按钮
    def MyBtn(self):
        try:
            __MyBtn=self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
        except Exception as err:
            assert False,\
            "定位我的按钮失败"
        return __MyBtn

    #定位获取用户名tit
    def text1(self):
        try:
            __text=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/nickname_tv")
        except Exception as err:
            assert False,\
            "获取用户名title失败"
        return __text

    #定位设置页按钮
    def setting(self):
        try:
            __setting=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/setting_tv")
        except Exception as err:
            assert False,\
            "定位设置按钮失败"
        return __setting

    #定位意见反馈
    def advice(self):
        try:
            __advice=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/tv_feedback")
        except Exception as err:
            assert False,\
            "定位意见反馈按钮失败"
        return __advice

    #定位个人中心
    def Mine_mine(self):
        try:
            __Mine_main=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/mine_main_ll")
        except Exception as err:
            assert False,\
            "定位个人中心失败"
        return __Mine_main

    #定位工作信息
    def Job_in(self):
        try:
            __Job_in=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位工作信息"
        return __Job_in