#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Camera(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位相机按钮
    def xiangji(self):
        try:
            __xiangji=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_camera_btn")
        except Exception as err:
            assert False,\
            "定位相机按钮"
        return __xiangji

