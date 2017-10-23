#coding:utf-8
#点击。。。后的浮窗
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class My_Headpage(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位从相册选择失败
    def Cong_Xz(self):
        try:
            __Cong_Xz=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位从相册选择失败"
        return __Cong_Xz

    #定位拍照
    def Pai_Zhao(self):
        try:
            __Pai_Zhao=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位拍照失败"
        return __Pai_Zhao

    #定位保存照片
    def Baoc_Zp(self):
        try:
            __Baoc_Zp=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位保存照片失败"
        return __Baoc_Zp

    #定位取消
    def quxiao(self):
        try:
            __quxiao=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[4]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位取消失败"
        return __quxiao