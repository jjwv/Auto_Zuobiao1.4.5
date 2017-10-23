#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class File(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位文件
    def wenjian(self):
        try:
            __wenjian=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_file_btn")
        except Exception as err:
            assert False,\
            "定位相机按钮"
        return __wenjian

    #定位本机文件页发送
    def send_btn(self):
        try:
            __send_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/send_btn")
        except Exception as err:
            assert False,\
            "定位本机文件页发送"
        return __send_btn

