#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Group_Data(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #联系人中群 鬼啦啦啦啦
    def Group_G(self):
        try:
            __Group_G=self.driver.find_elements_by_android_uiautomator('new UiSelector().text("拍照")')
        except Exception as err:
            assert False,\
            "定位联系人中群 鬼啦啦啦啦失败"
        return __Group_G
    #定位群头像
    def Group_head(self):
        try:
            __Group_head=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_head_iv")
        except Exception as err:
            assert False,\
            "定位群头像失败"
        return __Group_head

    #定位群成员
    def Group_member(self):
        try:
            __Group_member = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_member_tv")
        except Exception as err:
            assert False, \
            "定位群成员失败"
        return __Group_member

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

        # 定位菲姐
    def Fjie(self):
        try:
            __Fjie= self.driver.find_element_by_android_uiautomator('new UiSelector().text("菲姐")')
        except Exception as err:
            assert False, \
            "定位菲姐失败"
        return __Fjie

    #定位弹窗中确定
    def Qud(self):
        try:
            __Qud=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/positive_tv")
        except Exception as err:
            assert False, \
                "定位完成按钮失败"
        return __Qud

    # 定位弹窗中取消
    def Quxiao(self):
        try:
            __Quxiao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/negative_tv")
        except Exception as err:
            assert False, \
            "定位完成按钮失败"
        return __Quxiao



            #定位我的群名片
    def Member_name(self):
        try:
            __Member_name=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/member_name_arrow_iv")
        except Exception as err:
            assert False, \
                "定位我的群名片失败"
        return __Member_name
    #编辑群名片中的输入框
    def Member_et(self):
        try:
            __Member_et=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/member_name_et")
        except Exception as err:
            assert False, \
                "定位编辑群名片中的输入框失败"
        return __Member_et

    #定位群聊名称
    def Qlmc(self):
        try:
            __Qlmc=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_name_arrow_iv")
        except Exception as err:
            assert False, \
                "定位群聊名称失败"
        return __Qlmc

    #定位群聊名称   输入框
    def Qlmc_Srk(self):
        try:
            __Qlmc_Srk=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_name_et")
        except Exception as err:
            assert False, \
                "定位群聊名称   输入框失败"
        return __Qlmc_Srk

    #定位群二维码  保存到手机
    def Save_to_mobile(self):
        try:
            __Save_to_mobile=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/save_to_mobile_btn")
        except Exception as err:
            assert False, \
                "定位群二维码  保存到手机失败"
        return __Save_to_mobile
    #定位群二维码  分享二维码
    def Share_qr(self):
        try:
            __Share_qr=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/share_qr_code_btn")
        except Exception as err:
            assert False, \
                "定位群二维码  分享二维码失败"
        return __Share_qr

    #定位群公告
    def Group_notice(self):
        try:
            __Group_notice=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_notice_arrow_iv")
        except Exception as err:
            assert False, \
                "定位群公告失败"
        return __Group_notice
    #定位群公告中的输入框
    def Group_content(self):
        try:
            __Group_content=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/content_et")
        except Exception as err:
            assert False, \
                "定位群公告输入框失败"
        return __Group_content

    #定位我的群名片
    def Group_my_nickname(self):
        try:
            __Group_my_nickname=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_my_nickname_tv")
        except Exception as err:
            assert False, \
                "定位群名片失败"
        return __Group_my_nickname

    #定位编辑群名片  输入框
    def Member_name_et(self):
        try:
            __Member_name_et=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/member_name_et")
        except Exception as err:
            assert False, \
            "定位群名片  输入框失败"
        return __Member_name_et

    #定位  入群验证
    def Group_validate(self):
        try:
            __Group_validate=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/group_validate_sb")
        except Exception as err:
            assert False, \
                "定位  入群验证失败"
        return __Group_validate
    #群资料的聊天置顶
    def Chat_on_top(self):
        try:
            __Chat_on_top=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_on_top_sb")
        except Exception as err:
            assert False,\
            "点击定位置顶聊天失败"
        return __Chat_on_top

    #定位群资料消息免打扰
    def Message_no_disturb(self):
        try:
            __Message_no_disturb=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/message_no_disturb_sb")
        except Exception as err:
            assert False,\
            "点击定位群资料消息免打扰失败"
        return __Message_no_disturb

    #定位按群成员查找的输入框
    def Qsqk(self):
        try:
            __Qsqk=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        except Exception as err:
            assert False,\
            "定位按群成员查找的输入框失败"
        return __Qsqk

    #点击查找聊天记录
    def Find_chat_history(self):
        try:
            __Find_chat_history=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/find_chat_history_tv")
        except Exception as err:
            assert False, \
            "点击查找聊天记录失败"
        return __Find_chat_history


    #查找聊天记录的搜索框       取消按钮
    def Cancel_btn(self):
        try:
            __Cancel_btn=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/cancel_btn")
        except Exception as err:
            assert False, \
            "查找聊天记录的搜索框取消按钮"
        return __Cancel_btn


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

    #定位查找聊天文件按钮
    def Find_chat_file(self):
        try:
            __Find_chat_file=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/find_chat_file_tv")
        except Exception as err:
            assert False, \
            "定位查找聊天文件按钮"
        return __Find_chat_file

    #查找聊天记录的            搜索框
    def Search_edt(self):
        try:
            __Search_edt=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/search_edt")
        except Exception as err:
            assert False, \
            "查找聊天记录的搜索框"
        return __Search_edt

    # 定位举报
    def Complaint_tv(self):
        try:
            __Complaint_tv = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/report_tv")
        except Exception as err:
            assert False, \
            "定位  群资料中举报"
        return __Complaint_tv

    # 选择举报原因 骚扰广告
    def Saorao(self):
        try:
            __Saorao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/saorao_tv")
        except Exception as err:
            assert False, \
                "骚扰广告"
        return __Saorao

    # 选择举报原因 色情
    def Sqing(self):
        try:
            __Sqing = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/seqing_tv")
        except Exception as err:
            assert False, \
            "色情"
        return __Sqing

            # 选择举报原因 违法/政治敏感

    def Wfa(self):
        try:
            __Wfa = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/yaoyan_tv")
        except Exception as err:
            assert False, \
                "违法/政治敏感"
        return __Wfa

    # 选择举报原因 传播谣言
    def Cbyy(self):
        try:
            __Cbyy = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/yaoyan_tv")
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

    # 选择举报原因 冒充他人
    def Mctr(self):
        try:
            __Mctr = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/maochong_tv")
        except Exception as err:
            assert False, \
                "冒充他人"
        return __Mctr

    # 定位上传截图证明
    def Iv_img(self):
        try:
            __Iv_img = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/iv_img")
        except Exception as err:
            assert False, \
                "定位上传截图证明失败"
        return __Iv_img
    #定位补充说明
    def Ccsm(self):
        try:
            __Ccsm=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_text_cet")
        except Exception as err:
            assert False,\
            "定位补充说明失败"
        return __Ccsm

        # 定位红鲤鱼
    def Hongliyu(self):
        try:
            __Hongliyu= self.driver.find_element_by_android_uiautomator('new UiSelector().text("红鲤鱼与绿鲤鱼与驴")')
        except Exception as err:
            assert False, \
            "定位红鲤鱼与绿鲤鱼与驴失败"
        return __Hongliyu

    #定位设为管理员
    def Guanliyuan(self):
        try:
            __Guanliyuan=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/set_manager_sb")
        except Exception as err:
            assert False,\
            "定位设为管理员失败"
        return __Guanliyuan

    #定位设为群主
    def Shequnzhu(self):
        try:
            __Shequnzhu=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/set_master_sb")
        except Exception as err:
            assert False,\
            "定位设为群主失败"
        return __Shequnzhu

    #定位清空聊天记录
    def Clear_chat(self):
        try:
            __Clear_chat=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/clear_chat_history_tv")
        except Exception as err:
            assert False,\
            "定位清空聊天记录失败"
        return __Clear_chat

        # 定位宫雨菲非
    def Gongyuff(self):
        try:
            __Gongyuff= self.driver.find_element_by_android_uiautomator('new UiSelector().text("宫雨非非")')
        except Exception as err:
            assert False, \
            "定位宫雨菲非失败"
        return __Gongyuff

    #定位清空聊天激励
    def qingkongjl(self):
        try:
            __qingkongjl= self.driver.find_element_by_id('com.shixinyun.zuobiao:id/item_tv')
        except Exception as err:
            assert False, \
            "定位清空聊天记录"
        return __qingkongjl
