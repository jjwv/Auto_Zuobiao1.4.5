#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Picture(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位相册按钮
    def tupian(self):
        try:
            __tupian=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_image_btn")
        except Exception as err:
            assert False,\
            "定位相册失败"
        return __tupian

    #定位选择图片页完成按钮
    def fasong(self):
        try:
            __fasong=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_ok")
        except Exception as err:
            assert False,\
            "定位选择图片页完成按钮"
        return __fasong

    #定于预览按钮
    def yulan(self):
        try:
            __yulan= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btn_preview")
        except Exception as err:
            assert False, \
                "定于预览按钮失败"
        return __yulan


