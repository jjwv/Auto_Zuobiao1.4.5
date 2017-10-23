#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver

class Kankan_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #点击看看
    def Kankan_Anniu(self):
        try:
            __Kankan_Anniu = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/mine_aggregated_tv')
        except Exception as err:
            assert False, \
            "定位日程失败"
        return __Kankan_Anniu

    # 定位返回按钮
    def Back(self):
        try:
            __Back = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
                "定位返回按钮失败"
        return __Back

    # 定位完成按钮
    def Right(self):
        try:
            __Right = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
                "定位完成按钮失败"
        return __Right

    #定位换一批
    def Huanyipi(self):
        try:
            __Huanyipi = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/refresh_ll")
        except Exception as err:
            assert False, \
                "定位换一批"
        return __Huanyipi



