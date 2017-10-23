#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Data_Xingqing(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位返回按钮
    def Back(self):
        try:
            __Back=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "定位返回按钮失败"
        return __Back

    #定位完成按钮
    def Right(self):
        try:
            __Right=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
                "定位完成按钮失败"
        return __Right

    #点击设置备注名
    def Setting_Bzm(self):
        try:
            __Setting_Bzm=self.driver.find_elements_by_android_uiautomator('new UiSelector().text("设置备注名")')
        except Exception as err:
            assert False, \
                "点击设置备注名失败"
        return __Setting_Bzm
    #备注名描述输入框
    def Remark(self):
        try:
            __Remark=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_remark_edt")
        except Exception as err:
            assert False, \
                "备注名描述输入框失败"
        return __Remark
    #定位工作信息
    def Gzxx(self):
        try:
            __Gzxx=self.driver.find_elements_by_android_uiautomator('new UiSelector().text("工作信息")')
        except Exception as err:
            assert False,\
            "定位工作信息失败"
        return __Gzxx

    #定位描述
    def Ms(self):
        try:
            __Ms=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/remark_or_addition_tv1")
        except Exception as err:
            assert False, \
                "定位描述失败"
        return __Ms

    #定位...删除联系人
    def Delete(self):
        try:
            __Delete=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/delete_tv")
        except Exception as err:
            assert False, \
                "定位...删除联系人失败"
        return __Delete

    #定位浮窗取消按钮
    def Fcqx(self):
        try:
            __Fcqx=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False, \
                "定位浮窗取消按钮失败"
        return __Fcqx
    #点击。。中的举报
    def Jubao(self):
        try:
            __Jubao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/report_tv")
        except Exception as err:
            assert False, \
                "点击。。中的举报失败"
        return __Jubao

    #设置备注名
    def beizhum(self):
        try:
            __beizhum=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "点击备注名失败"
        return __beizhum

    #工作信息
    def gongzuoxinx(self):
        try:
            __gongzuoxinx=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "点击工作信息失败"
        return __gongzuoxinx

