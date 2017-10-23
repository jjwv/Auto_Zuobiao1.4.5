#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class GlfzPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #管理分组页 添加分组
    def Tjfz(self):
        try:
            __Tjfz=self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加分组")')
        except Exception as err:
            assert False,\
            "定位管理分组页 添加分组失败"
        return __Tjfz

    #定位输入分组名称的输入框
    def Qsr(self):
        try:
            __Qsr=self.driver.find_element_by_class_name("android.widget.EditText")
        except Exception as err:
            assert False,\
            "定位输入分组名称的输入框失败"
        return __Qsr

    #定位输入分组名称时的确定按钮
    def Qding(self):
        try:
            __Qding=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/tv_confirm")
        except Exception as err:
            assert False,\
            "定位输入分组名称时的确定按钮失败"
        return __Qding
    #定位完成按钮
    def Complete(self):
        try:
            __Complete=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False,\
            "定位定位完成按钮失败"
        return __Complete

    #点击         删除分组
    def Delete_Group(self):
        try:
            __Delete_Group=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/item_tv")
        except Exception as err:
            assert False,\
            "点击         删除分组失败"
        return __Delete_Group