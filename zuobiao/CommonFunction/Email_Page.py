#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
class Email_Page(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

    #定位邮件
    def Email(self):
        try:
            __Email=self.driver.find_element_by_id('com.shixinyun.zuobiao:id/mine_email_ll')
        except Exception as err:
            assert False,\
            "定位邮件失败"
        return __Email

    #定位添加邮箱账号
    def Add_Email(self):
        try:
            __Add_Email=self.driver.find_element_by_id('com.shixinyun.zuobiao:id/add_email_account_btn')
        except Exception as err:
            assert False,\
            "定位添加邮箱账号"
        return __Add_Email

    #定位添加邮箱账号页的账号输入框
    def ZH_shuruk(self):
        try:
            __Zh_shuruk = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/input_email_account_et')
        except Exception as err:
            assert False, \
                "定位添加邮箱账号页的账号输入框"
        return __Zh_shuruk

    #定位添加邮箱账号页的密码  输入框
    def MM_shuruk(self):
        try:
            __MM_shuruk = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/input_email_password_et')
        except Exception as err:
            assert False, \
                "定位添加邮箱账号页的密码  输入框"
        return __MM_shuruk

    # 定位添加邮箱账号页的确定按钮
    def QD(self):
        try:
            __QD = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/confirm_btn')
        except Exception as err:
            assert False, \
                "定位定位添加邮箱账号页的确定按钮"
        return __QD

    # 定位添加失败页面中的手动设置
    def Shoudongsz(self):
        try:
            __Shoudongsz= self.driver.find_element_by_id('android:id/button2')
        except Exception as err:
            assert False, \
                "定位添加失败页面中的手动设置"
        return __Shoudongsz
    # 定位添加失败页面中的确定按钮
    def Tjsb_Qd(self):
        try:
            __Tjsb_Qd = self.driver.find_element_by_id('android:id/button1')
        except Exception as err:
            assert False, \
                "定位添加失败页面中的确定按钮"
        return __Tjsb_Qd

    #定位邮件中的加号
    def Email_Jiahao(self):
        try:
            __Email_Jiahao = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/notify_iv')
        except Exception as err:
            assert False, \
                "定位邮件中的加号"
        return __Email_Jiahao

    #定位邮件加号 写邮件
    def Xieyoujian(self):
        try:
            __Xieyoujian = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/write_mails_tv')
        except Exception as err:
            assert False, \
                "定位邮件加号 写邮件"
        return __Xieyoujian

    # 定位邮件加号 账号管理
    def Zhanghaogl(self):
        try:
            __Zhanghaogl = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/manage_mail_account_tv')
        except Exception as err:
            assert False, \
                "定位邮件加号 账号管理"
        return __Zhanghaogl

    #定位发送邮件页 收件人输入框
    def shoujianren(self):
        try:
            __shoujianren = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/receiver_edt')
        except Exception as err:
            assert False, \
                "定位发送邮件页 收件人输入框"
        return __shoujianren
    #定位发送邮件页  抄送输入框
    def Chaosong(self):
        try:
            __Chaosong = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/copy_to_edt')
        except Exception as err:
            assert False, \
                "定位发送邮件页  抄送输入框"
        return __Chaosong
    #定位发送邮件页  主题输入框
    def Zhuti(self):
        try:
            __Zhuti = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/theme_edt')
        except Exception as err:
            assert False, \
                "定位发送邮件页  主题输入框"
        return __Zhuti
    #定位发送邮件页  正文输入框
    def Zhengwen(self):
        try:
            __Zhengwen = self.driver.find_element_by_class_name('android.webkit.WebView')
        except Exception as err:
            assert False, \
                "定位发送邮件页  正文输入框"
        return __Zhengwen

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

    #定位提示框中的确定
    def Tishikuang_Qd(self):
        try:
            __Tishikuang=self.driver.find_element_by_id("android:id/button1")
        except Exception as err:
            assert False, \
                "定位提示框中的确定"
        return __Tishikuang

    #定位删除草稿
    def Shanchucaogao(self):
        try:
            __Shanchucaogao=self.driver.find_element_by_id("android:id/button2")
        except Exception as err:
            assert False, \
                "定位删除草稿"
        return __Shanchucaogao
    #定位保存草稿
    def Baocuncg(self):
        try:
            __Baocuncg=self.driver.find_element_by_id("android:id/button1")
        except Exception as err:
            assert False, \
                "定位保存草稿"
        return __Baocuncg

    #点击以保存的第一个账号
    def Zhanghaogl_Zz(self):
        try:
            __Zhanghaogl_Zz=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/mail_account_tv")
        except Exception as err:
            assert False, \
                "定位以保存的第一个账号"
        return __Zhanghaogl_Zz

    #定位删除账号
    def Shanchuzhanghao(self):
        try:
            __Shanchuzhanghao=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/delete_mail_account_btn")
        except Exception as err:
            assert False, \
                "定位删除账号"
        return __Shanchuzhanghao
    # 定位弹窗删除账号
    def Tanchuang_Shanchuzhanghao(self):
        try:
            __TanChuang_Shanchuzhanghao = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/item_tv")
        except Exception as err:
            assert False, \
                "定位弹窗删除账号"
        return __TanChuang_Shanchuzhanghao

    #定位添加邮箱账号
    def Tianjiazhanghao(self):
        try:
            __Tianjiazhanghao= self.driver.find_element_by_id("com.shixinyun.zuobiao:id/add_mail_account_btn")
        except Exception as err:
            assert False, \
                "定位添加邮箱账号"
        return __Tianjiazhanghao

    #定位账号title
    def Zhanghao_Title(self):
        try:
            __Zhanghao_Title= self.driver.find_element_by_id('com.shixinyun.zuobiao:id/cube_title')
        except Exception as err:
            assert False,\
            "定位账号title"
        return __Zhanghao_Title

    #定位账号title下添加邮箱账号
    def Title_Tianjiazhanghao(self):
        try:
            __Title_Tianjiazhanghao=self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加邮箱账号")')
        except Exception as err:
            assert False,\
            "定位账号title下添加邮箱账号"
        return __Title_Tianjiazhanghao

    #定位邮件中的转发
    def Zhuanfa(self):
        try:
            __Zhuanfa= self.driver.find_element_by_id('com.shixinyun.zuobiao:id/mail_forward_tv')
        except Exception as err:
            assert False,\
            "定位邮件中的转发"
        return __Zhuanfa
    #定位邮件中的回复
    def Huifu(self):
        try:
            __Huifu= self.driver.find_element_by_id('com.shixinyun.zuobiao:id/mail_reply_tv')
        except Exception as err:
            assert False,\
            "定位邮件中的回复"
        return __Huifu

    #定位浮窗的回复
    def Fuchaugn_Huifu(self):
        try:
            __Fuchaung_Huifu=self.driver.find_element_by_android_uiautomator('new UiSelector().text("回复")')
        except Exception as err:
            assert False,\
            "定位浮窗的回复"
        return __Fuchaung_Huifu
    #定位浮窗的全部回复
    def Fuchaugn_Quanbuhuifu(self):
        try:
            __Fuchuang_Quanbuhuifu=self.driver.find_element_by_android_uiautomator('new UiSelector().text("全部回复")')
        except Exception as err:
            assert False,\
            "定位浮窗的全部回复"
        return __Fuchuang_Quanbuhuifu



