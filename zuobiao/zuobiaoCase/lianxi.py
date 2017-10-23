#coding:utf-8
from appium import webdriver

import time

desired_caps = {}
desired_caps['device'] = "PD1602"
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "5.1.1"
desired_caps['deviceName'] = "vivo_X7"

desired_caps['unicodeKeyboard'] = "True"
desired_caps['resetKeyboard'] = "True"
# 通过IP+端口号连接appium(/wd/hub是固定不变的），通过手机设备信息连接手机
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(3)
driver.find_element_by_id("com.shixinyun.zuobiao:id/skip_btn").click()
driver.find_element_by_id("com.shixinyun.zuobiao:id/account_et").send_keys("13691515688")
time.sleep(1)
driver.find_element_by_id("com.shixinyun.zuobiao:id/password_et").send_keys("123456")
time.sleep(2)
driver.find_element_by_id("com.shixinyun.zuobiao:id/login_btn").click()
time.sleep(4)
#新手教程
driver.find_element_by_id("com.shixinyun.zuobiao:id/guide_close_tv").click()
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("联系人")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('new UiSelector().text("我的好友")').click()
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("红鲤鱼与绿鲤鱼与驴")').click()
time.sleep(2)
driver.find_element_by_id("com.shixinyun.zuobiao:id/send_message_layout").click()
time.sleep(2)
driver.find_element_by_id("com.shixinyun.zuobiao:id/chat_voice_btn").click()
time.sleep(2)







