#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Face(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位表情按钮
    def biaoqing(self):
        try:
            __biaoqing=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_face_btn")
        except Exception as err:
            assert False,\
            "定位表情按钮失败"
        return __biaoqing
