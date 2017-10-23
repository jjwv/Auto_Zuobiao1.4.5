#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Top(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    # 消息页面搜索  放大镜按钮
    def Fangdajing(self):
        try:
            __Fangdajing = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/logo")
        except Exception as err:
            assert False, \
            "定位消息页面搜索  放大镜按钮失败"
        return __Fangdajing

    #点击放大镜点击进入的搜索框
    def Sousu(self):
        __Sousu=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_layout")
        return __Sousu

#点击铃铛内小人头添加联系人页面中的搜索框
    def Sousu_T(self):
        __Sousu_T=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_tv")
        return __Sousu_T

    #在搜索框搜索
    def Zsousu(self):
        __Zsousu=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        return __Zsousu

    #在搜索框取消
    def Cancel(self):
        __Cancel=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        return __Cancel

    #点击联系人搜索
    def Contact_btn(self):
        try:
            __Contact_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/contact_btn")
        except Exception as err:
            assert False, \
            "定位点击联系人搜索失败"
        return __Contact_btn

    #点击聊天记录搜索
    def Chat_record(self):
        try:
            __Chat_record=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_record_btn")
        except Exception as err:
            assert False, \
            "定位点击聊天记录搜索失败"
        return __Chat_record

    #点击按文件搜索
    def File_btn(self):
        try:
            __File_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/file_btn")
        except Exception as err:
            assert False, \
            "定位点击按文件搜索失败"
        return __File_btn
    #定位铃铛进入验证信息
    def Notify(self):
        try:
            __Notify=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/notify_iv")
        except Exception as err:
            assert False, \
            "定位铃铛进入验证信息失败"
        return __Notify

    # 验证消息页面中返回按钮
    def Back(self):
        try:
            __Back = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "验证消息页面中返回按钮失败"
        return __Back

    #验证消息页面中添加联系人  小人头按钮
    def Tjlxr(self):
        try:
            __Tjlxr = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
            "验证消息页面中添加联系人  小人头按钮"
        return __Tjlxr

    #点击加号后点击创建群组
    def Creat_group(self):
        try:
            __Creat_group=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/create_group_tv")
        except Exception as err:
            assert False,\
            "点击加号后点击创建群组"
        return __Creat_group

    #创建群组后点击小人头进去群资料页退出群组
    def Exit_group(self):
        try:
            __Exit_group = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/exit_group_btn")
        except Exception as err:
            assert False, \
            "创建群组后点击小人头进去群资料页退出群组失败"
        return __Exit_group

    #解散群
    def Jsq(self):
        try:
            __Jsq=self.driver.find_elements_by_android_uiautomator('new UiSelector().text("解散")')
        except Exception as err:
            assert False, \
            "解散群失败"
        return __Jsq
    #弹出解散窗口点击确定
    def Fcqd(self):
        try:
            __Fcqd=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/positive_tv")
        except Exception as err:
            assert False, \
            "弹出解散窗口点击确定失败"
        return __Fcqd

    #点击加号后点击添加联系人
    def Add_friend(self):
        try:
            __Add_friend=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/add_friend_tv")
        except Exception as err:
            assert False, \
            "点击加号后点击添加联系人失败"
        return __Add_friend

    #点击添加联系人页中搜索框
    def Tjiasou(self):
        try:
            __Tjiasou=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_tv")
        except Exception as err:
            assert False, \
            "点击添加联系人页中搜索框失败"
        return __Tjiasou

    #添加联系人中点击我的二维码
    def My_qr(self):
        try:
            __My_qr=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/my_qr_img_iv")
        except Exception as err:
            assert False, \
            "点击添加联系人中点击我的二维码失败"
        return __My_qr

    #添加联系人中 点击添加手机联系人
    def Add_mobile(self):
        try:
            __Add_mobile=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/add_mobile_contact_layout")
        except Exception as err:
            assert False, \
            "添加联系人中 点击添加手机联系人失败"
        return __Add_mobile

    #点击加号 扫一扫
    def Scan_tv(self):
        try:
            __Scan_tv=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/scan_tv")
        except Exception as err:
            assert False, \
            "点击加号 扫一扫失败"
        return __Scan_tv

    #扫一扫群名片，打开群详情
    def Join_group(self):
        try:
            __Join_group=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/join_group_btn")
        except Exception as err:
            assert False, \
            "扫一扫群名片，打开群详情失败"
        return __Join_group

    #定位top加号
    def Jiahao(self):
        try:
            __Jiahao=self.driver.find_element("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
        except Exception as err:
            assert False, \
            "定位top加号失败"
        return __Jiahao

    #定位群组小人头进入群资料
    def Jqunzuzl(self):
        try:
            __Jqunzuzl=self.driver.find_element(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
        except Exception as err:
            assert False, \
            "定位群组小人头进入群资料失败"
        return __Jqunzuzl

    #定位群资料退出群 解散群
    def Jsanqun(self):
        try:
            __Jsanqun=self.driver.find_element("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
            "定位群资料退出群 解散群失败"
        return __Jsanqun

    #定位群资料退出群 解散群
    def Jsanqun(self):
        try:
            __Jsanqun=self.driver.find_element("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
            "定位群资料退出群 解散群失败"
        return __Jsanqun


    #添加联系人搜索点击搜索接口框
    def Soulxrk(self):
        try:
            __Soulxrk = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]")
        except Exception as err:
            assert False, \
                "定位添加联系人搜索点击搜索接口框失败"
        return __Soulxrk

   #扫一扫相册按钮
    def Sysxiangce(self):
        try:
            __Sysxiangce = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]")
        except Exception as err:
            assert False, \
                "定位扫一扫相册按钮败"
        return __Sysxiangce

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