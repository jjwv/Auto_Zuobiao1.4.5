#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Choose_Group(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    # 选择分组页  选择哈哈哈分组
    def Haha(self):
        try:
            __Haha=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "选择哈哈哈分组失败"
        return __Haha

    #选择删除哈哈哈分组
    def shanchuhaha(self):
        try:
            __shanchuhaha=self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[3]/android.widget.ImageView[1]")
        except Exception as err:
            assert False,\
            "选择删除哈哈哈分组失败"
        return __shanchuhaha