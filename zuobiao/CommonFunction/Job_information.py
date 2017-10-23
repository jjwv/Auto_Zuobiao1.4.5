#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Job_information(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位行业
    def Industry(self):
        try:
            __Industry=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/industry_iv")
        except Exception as err:
            assert False,\
            "定位行业失败"
        return __Industry

    #定位公司
    def Company(self):
        try:
            __Company=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/company_iv")
        except Exception as err:
            assert False,\
            "定位公司失败"
        return __Company

    #定位职位
    def Position(self):
        try:
            __Position=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/position_iv")
        except Exception as err:
            assert False,\
            "定位职位失败"
        return __Position


    #定位计算机/互联网
    def Jsuanji(self):
        try:
            __Jsuanji=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位计算机/互联网失败"
        return __Jsuanji
   #定位电子商务
    def Dianzishangwu(self):
        try:
            __Dianzishangwu=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位电子商务失败"
        return __Dianzishangwu

   #定位公司输入框
    def Gshurukuang(self):
        try:
            __Gshurukuang=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/nickname_edt")
        except Exception as err:
            assert False,\
            "定位公司输入框失败"
        return __Gshurukuang


