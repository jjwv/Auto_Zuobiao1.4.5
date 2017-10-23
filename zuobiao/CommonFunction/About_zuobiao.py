#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class About_zuobiao(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位服务协议
    def Service_agreement(self):
        try:
            __Service_agreement=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/service_agreement_tv")
        except Exception as err:
            assert False,\
            "定位服务协议失败"
        return __Service_agreement

    #定位意见反馈
    def Feedback_tv(self):
        try:
            __Feedback_tv=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/feedback_tv")
        except Exception as err:
            assert False,\
            "定位意见反馈失败"
        return __Feedback_tv


    # 定位意见反馈输入框
    def Feedback_et(self):
        try:
            __Feedback_et = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/feedback_et")
        except Exception as err:
            assert False, \
                "定位意见反馈输入框失败"
        return __Feedback_et

    # 定位意见反馈输入框  提交按钮
    def Commit_btn(self):
        try:
            __Commit_btn = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/commit_btn")
        except Exception as err:
            assert False, \
                "定位意见反馈输入框  提交按钮失败"
        return __Commit_btn


