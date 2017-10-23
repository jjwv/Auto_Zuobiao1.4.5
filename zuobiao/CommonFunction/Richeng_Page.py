#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver

class Richeng_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位日程
    def Richeng(self):
        try:
            __Richeng=self.driver.find_element_by_id('com.shixinyun.zuobiao:id/mine_schedule_tv')
        except Exception as err:
            assert False,\
            "定位日程失败"
        return __Richeng

    #定位返回按钮
    def Back(self):
        try:
            __Back=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "定位返回按钮失败"
        return __Back

    #定位完成按钮
    def Right(self):
        try:
            __Right=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
                "定位完成按钮失败"
        return __Right


    #定位日程输入框
    def Ric_Shuruk(self):
        try:
            __Ric_Shutuk=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/content_et")
        except Exception as err:
            assert False, \
                "定位日程输入框"
        return __Ric_Shutuk
    #定位开始按钮
    def Kaishi(self):
        try:
            __Kaishi=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/start_rl")
        except Exception as err:
            assert False, \
                "定位开始按钮"
        return __Kaishi
    #定位结束按钮
    def Jieshu(self):
        try:
            __Jieshu=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/end_rl")
        except Exception as err:
            assert False, \
                "定位结束按钮"
        return __Jieshu
    #定位提醒按钮
    def Tixing(self):
        try:
            __Tixing=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/remind_rl")
        except Exception as err:
            assert False, \
                "定位提醒按钮"
        return __Tixing


    #定位开始、结束、提醒按钮中的完成
    def Wancheng(self):
        try:
            __Wancheng=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/submit_tv")
        except Exception as err:
            assert False, \
                "定位开始、结束、提醒按钮中的完成"
        return __Wancheng
    #定位开始、结束、提醒按钮中的取消
    def Quxiao(self):
        try:
            __Quxiao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_tv")
        except Exception as err:
            assert False, \
                "定位开始、结束、提醒按钮中的取消"
        return __Quxiao

    #定位取消日程的小方框
    def Qx_Fangkuang(self):
        try:
            __Qx_Fangkuang=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/checked_iv")
        except Exception as err:
            assert False, \
                "定位取消日程的小方框"
        return __Qx_Fangkuang

    #定位删除日程
    def Shanchuricheng(self):
        try:
            __Shanchuricheng=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/delete_btn")
        except Exception as err:
            assert False, \
                "定位删除日程"
        return __Shanchuricheng

    # 点击弹窗中的删除
    def Tanchuang_Shanchu(self):
        try:
            __Tanchuang_Shanchu=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/item_tv")
        except Exception as err:
            assert False, \
                "点击弹窗中的删除"
        return __Tanchuang_Shanchu

    # 点击搜索框中的输入框
    def Sousu_Shurukuang(self):
        try:
            __Sousu_Shurukuang=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        except Exception as err:
            assert False, \
                "点击搜索框中的输入"
        return __Sousu_Shurukuang
    # 点击搜索框中的取消
    def Sousu_Quxiao(self):
        try:
            __Sousu_Quxiao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False, \
                "点击搜索框中的取消"
        return __Sousu_Quxiao








