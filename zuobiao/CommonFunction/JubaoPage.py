#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class JUbaoPage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    # 定位上传截图 拍照
    def Pai(self):
        try:
            __Pai = self.driver.find_elements_by_android_uiautomator('new UiSelector().text("拍照")')
        except Exception as err:
            assert False, \
            "定位上传截图证明失败"
        return __Pai

    # 定位上传截图 图片图库
    def Tupintk(self):
        try:
            __Tupintk = self.driver.find_elements_by_android_uiautomator('new UiSelector().text("图片图库")')
        except Exception as err:
            assert False, \
            "定位上传截图 图片图库失败"
        return __Tupintk

    # 定位上传截图 取消
    def Quxiao(self):
        try:
            __Quxiao = self.driver.find_elements_by_android_uiautomator('new UiSelector().text("取消")')
        except Exception as err:
            assert False, \
            "定位上传截图 取消失败"
        return __Quxiao