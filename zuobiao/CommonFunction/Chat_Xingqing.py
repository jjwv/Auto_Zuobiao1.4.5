#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Chat_Xingqing(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位小人头进去资料详情页
    def Xiaorentou(self):
        try:
            __Xiaorentou=self.driver.find_element_by_class_name("android.widget.ImageView")
        except Exception as err:
            assert False,\
            "定位小人头进去资料详情页"
        return __Xiaorentou

    #定位点击加号添加群组聊天
    def Add_user(self):
        try:
            __Add_user=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/add_user_iv")
        except Exception as err:
            assert False,\
            "点击加号添加群组聊天"
        return __Add_user

        # 定位菲姐
    def Fjie(self):
        try:
            __Fjie= self.driver.find_element_by_android_uiautomator('new UiSelector().text("菲姐")')
        except Exception as err:
            assert False, \
            "定位菲姐失败"
        return __Fjie

    # 定位宫雨非非
    def Gfei(self):
        try:
            __Gfei= self.driver.find_element_by_android_uiautomator('new UiSelector().text("宫雨非非")')
        except Exception as err:
            assert False, \
            "定位宫雨非非失败"
        return __Gfei
    #选择联系人后点击确定
    def Right(self):
        try:
            __Right= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False, \
            "选择联系人后点击确定"
        return __Right
    #点击创建群组返回键
    def Back(self):
        try:
            __Back= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "点击创建群组返回键失败"
        return __Back

    #定位置顶聊天
    def Top_chat(self):
        try:
            __Top_chat=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/top_chat_sb")
        except Exception as err:
            assert False,\
            "点击定位置顶聊天失败"
        return __Top_chat

    #定位消息免打扰
    def Not_disturb(self):
        try:
            __Not_disturb=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/not_disturb_sb")
        except Exception as err:
            assert False,\
            "点击定位消息免打扰失败"
        return __Not_disturb

    #点击查找聊天记录
    def Find_chat_history(self):
        try:
            __Find_chat_history=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/find_chat_history_tv")
        except Exception as err:
            assert False, \
            "点击查找聊天记录失败"
        return __Find_chat_history

    #定位按日期查找
    def Anriqi(self):
        try:
            __Anriqi=self.driver.find_element_by_class_name("android.widget.ImageView")
        except Exception as err:
            assert False, \
            "定位按日期查找失败"
        return __Anriqi

    #点击按日期查找                返回
    def Id_back(self):
        try:
            __Id_back=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/back")
        except Exception as err:
            assert False, \
            "点击返回失败"
        return __Id_back

    #查找聊天记录的            搜索框
    def Search_edt(self):
        try:
            __Search_edt=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        except Exception as err:
            assert False, \
            "查找聊天记录的搜索框"
        return __Search_edt

    #查找聊天记录的搜索框       取消按钮
    def Cancel_btn(self):
        try:
            __Cancel_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False, \
            "查找聊天记录的搜索框取消按钮"
        return __Cancel_btn

    #定位查找聊天文件按钮
    def Find_chat_file(self):
        try:
            __Find_chat_file=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/find_chat_file_tv")
        except Exception as err:
            assert False, \
            "定位查找聊天文件按钮"
        return __Find_chat_file

    #定位聊天文件中的搜索框
    def Search_layout(self):
        try:
            __Search_layout=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_layout")
        except Exception as err:
            assert False, \
            "定位聊天文件中的搜索框"
        return __Search_layout

    #定位聊天文件页图片/视频
    def Picture_shipin(self):
        try:
            __Picture_shipin= self.driver.find_element_by_android_uiautomator('new UiSelector().text("图片/视频")')
        except Exception as err:
            assert False, \
            "定位聊天文件页图片/视频"
        return __Picture_shipin

    #定位文档
    def File_s(self):
        try:
            __File_s= self.driver.find_element_by_android_uiautomator('new UiSelector().text("文档")')
        except Exception as err:
            assert False, \
            "定位文档"
        return __File_s

    #定位其他
    def Qita(self):
        try:
            __Qita= self.driver.find_element_by_android_uiautomator('new UiSelector().text("其他")')
        except Exception as err:
            assert False, \
            "定位其他"
        return __Qita

    #定位举报
    def Complaint_tv(self):
        try:
            __Complaint_tv= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/complaint_tv")
        except Exception as err:
            assert False, \
            "定位举报"
        return __Complaint_tv

    #选择举报原因 骚扰广告
    def Saorao(self):
        try:
            __Saorao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/saorao_tv")
        except Exception as err:
            assert False, \
            "骚扰广告"
        return __Saorao

    #选择举报原因 色情
    def Sqing(self):
        try:
            __Sqing=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/seqing_tv")
        except Exception as err:
            assert False, \
            "色情"
        return __Sqing

 # 选择举报原因 违法/政治敏感
    def Wfa(self):
        try:
            __Wfa=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/yaoyan_tv")
        except Exception as err:
            assert False, \
            "违法/政治敏感"
        return __Wfa

    #选择举报原因 传播谣言
    def Cbyy(self):
        try:
            __Cbyy=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/yaoyan_tv")
        except Exception as err:
            assert False, \
            "违法/政治敏感"
        return __Cbyy

    # 选择举报原因 欺骗
    def Qpian(self):
        try:
            __Qpian = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/qizha_tv")
        except Exception as err:
            assert False, \
            "欺骗"
        return __Qpian
    #选择举报原因 冒充他人
    def Mctr(self):
        try:
            __Mctr= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/maochong_tv")
        except Exception as err:
            assert False, \
            "冒充他人"
        return __Mctr




    #定位上传截图证明
    def Iv_img(self):
        try:
            __Iv_img=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/iv_img")
        except Exception as err:
            assert False,\
            "定位上传截图证明失败"
        return __Iv_img

    #定位上传截图 拍照
    def Zhaopai(self):
        try:
            __Zhaopai=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位上传截图证明  拍照失败"
        return __Zhaopai

    #定位上传截图 图片图库
    def Tupintk(self):
        try:
            __Tupintk=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位上传截图 图片图库失败"
        return __Tupintk

    #定位上传截图 取消
    def Quxiao(self):
        try:
            __Quxiao=self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位上传截图 取消失败"
        return __Quxiao





    #定位补充说明
    def Ccsm(self):
        try:
            __Ccsm=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_text_cet")
        except Exception as err:
            assert False,\
            "定位补充说明失败"
        return __Ccsm

    #点击提交按钮
    def Right_tijao(self):
        try:
            __Right_tijiao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/right")
        except Exception as err:
            assert False,\
            "点击提交按钮"
        return __Right_tijiao

    #点击提交后弹出窗的确定
    def Button(self):
        try:
            __Button=self.driver.find_element_by_id("android:id/button1")
        except Exception as err:
            assert False,\
            "点击提交后弹出窗的确定"
        return __Button

    #资料详情页换分组按钮
    def Hfz(self):
        try:
            __Hfz=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/organize_tv")
        except Exception as err:
            assert False,\
            "资料详情页换分组按钮"
        return __Hfz





