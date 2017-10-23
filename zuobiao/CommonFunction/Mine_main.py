#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
import sys,os
sys.path.append(os.getcwd())
class Mine_main(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver

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

    # 定位头像
    def Head(self):
        try:
            __Head = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/head_iv")
        except Exception as err:
            assert False, \
            "定位头像失败"
        return __Head

    #定位昵称
    def UserName(self):
        try:
            __UserName = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/username_tv")
        except Exception as err:
            assert False, \
            "定位昵称失败"
        return __UserName
    #定位昵称的输入框
    def Input_nickname(self):
        try:
            __Input_nickname = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_nickname_cet")
        except Exception as err:
            assert False, \
            "定位昵称的输入框失败"
        return __Input_nickname

   #定位二维码名片
    def Qr_code_ll(self):
        try:
            __Qr_code_ll = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/qr_code_ll")
        except Exception as err:
            assert False, \
            "定位二维码名片失败"
        return __Qr_code_ll

    #定位群二维码  保存到手机
    def Save_to_mobile(self):
        try:
            __Save_to_mobile=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/save_to_mobile_btn")
        except Exception as err:
            assert False, \
                "定位  保存到手机失败"
        return __Save_to_mobile
    #定位群二维码  分享二维码
    def Share_qr(self):
        try:
            __Share_qr=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/share_qr_code_btn")
        except Exception as err:
            assert False, \
                "定位  分享二维码失败"
        return __Share_qr

    #定位性别
    def Gender_tv(self):
        try:
            __Gender_tv=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/gender_tv")
        except Exception as err:
            assert False, \
                "定位  性别"
        return __Gender_tv
    #定位性别女
    def Nv(self):
        try:
            __Nv=self.driver.find_elements_by_xpath(" //android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位性别女失败"
        return __Nv
    #定位性别男
    def Nan(self):
        try:
            __Nan=self.driver.find_elements_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False,\
            "定位性别男失败"
        return __Nan

    #定位生日
    def Birthday(self):
        try:
            __Birthday=self.driver.find_element_by_id("com.shixinyun.zuobiao:id/birthday_tv")
        except Exception as err:
            assert False, \
                "定位生日失败"
        return __Birthday
    #定位生日浮窗页的确定
    def BtnSubmit(self):
        try:
            __BtnSubmit = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btnSubmit")
        except Exception as err:
            assert False, \
                "定位生日浮窗页的确定失败"
        return __BtnSubmit
    #定位生日浮窗页的取消
    def BtnCancel(self):
        try:
            __BtnCancel = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/btnCancel")
        except Exception as err:
            assert False, \
                "定位定位生日浮窗页的取消失败"
        return __BtnCancel


    #定位地区
    def Area(self):
        try:
            __Area = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/area_tv")
        except Exception as err:
            assert False, \
                "定位地区失败"
        return __Area

    # 定位电话
    def Iphone(self):
        try:
            __IPhone = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "定位电话失败"
        return __IPhone

    #定位邮箱
    def Email(self):
        try:
            __Email = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[4]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "定位邮箱失败"
        return __Email

    #定位电话输入框
    def Dsrk(self):
        try:
            __Dsrk = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_mobile_cet")
        except Exception as err:
            assert False, \
                "定位电话输入框失败"
        return __Dsrk
 #定位邮箱输入框
    def Ysrk(self):
        try:
            __Ysrk = self.driver.find_element_by_id("com.shixinyun.zuobiao:id/input_email_cet")
        except Exception as err:
            assert False, \
                "定位电话输入框失败"
        return __Ysrk

 #定位性别男女
    def nan(self):
        try:
            __nan = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "定位性别男失败"
        return __nan

 #定位性别男女
    def nv(self):
        try:
            __nv = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        except Exception as err:
            assert False, \
                "定位性别男失败"
        return __nv

