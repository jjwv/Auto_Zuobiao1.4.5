from Utills.GetAppiumDriver import GetAppiumDriver
class Duorenyy_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位鬼啦啦啦群组
    def Guilala(self):
        try:
            __Guilala = self.driver.find_element_by_android_uiautomator('new UiSelector().text("鬼啦啦啦啦")')
        except Exception as err:
            assert False, \
                "定位鬼啦啦啦群组"
        return __Guilala

    #定位群组的加号
    def Quzujiahao(self):
        try:
            __Quzujiahao=self.driver.find_element_by_id('com.shixinyun.zuobiao:id/chat_more_btn')
        except Exception as err:
            assert False,\
            "定位群组的加号"
        return __Quzujiahao

    #定位语音通话
    def Yuyinth(self):
        try:
            __Yuyinth = self.driver.find_element_by_android_uiautomator('new UiSelect().text("语音通话")')
        except Exception as err:
            assert False, \
                "定位语音通话"
        return __Yuyinth

    # 定位完成按钮
    def Right(self):
        try:
            __Right = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
            "定位完成按钮失败"
        return __Right

    # 定位返回按钮
    def Back(self):
        try:
         __Back = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "定位返回按钮失败"
        return __Back

    #定位免提按钮
    def mianti(self):
        try:
            __mianti = self.driver.find_element_by_android_uiautomator('new UiSelector().text("免提")')
        except Exception as err:
            assert False, \
                "定位免提按钮"
        return __mianti

    #定位多人语音收缩按钮
    def Shousuo(self):
        try:
            __Shousuo=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_group_zoom_btn")
        except Exception as err:
            assert False,\
            "定位多人语音收缩按钮"
        return __Shousuo

    #定位挂断按钮
    def Guaduan(self):
        try:
            __Guaduan=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_group_hang_up_btn")
        except Exception as err:
            assert False,\
            "定位挂断按钮"
        return __Guaduan

    #定位多人语音中添加人加号按钮
    def Duorenyy_jiahao(self):
        try:
            __Duorenyy_jiahao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/call_group_add_btn")
        except Exception as err:
            assert False,\
            "定位多人语音中添加人加号按钮"
        return __Duorenyy_jiahao