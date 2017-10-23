#-*- coding:UTF-8 -*-
import sys,os
sys.path.append(os.getcwd())
from appium import webdriver
from Utills.Common import singleton
@singleton
class GetAppiumDriver(object):
    def __init__(self):
        desired_caps={}
        desired_caps['device'] = "PD1602"
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = "5.1.1"
        desired_caps['deviceName'] = "vivo_X7"

        desired_caps['unicodeKeyboard']="True"
        desired_caps['resetKeyboard']="True"
        # 通过IP+端口号连接appium(/wd/hub是固定不变的），通过手机设备信息连接手机
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)


