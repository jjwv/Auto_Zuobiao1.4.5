#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from appium.webdriver.common.touch_action import TouchAction
import sys,os
sys.path.append(os.getcwd())
class GetAppiumHelp(object):
    def __init__(self):#初始化
        global x,y#全局变量
        self.driver=GetAppiumDriver().driver
        #屏幕大小
        x=self.driver.get_window_size()["width"]#宽
        y=self.driver.get_window_size()["height"]#高

    def LeftToRight(self):#从左向右划
        self.driver.swipe(x/9,y/2,x*0.9,y/2,500)#输入坐标x,y,时间
    def RightToLeft(self):#起点不能从边开始
         self.driver.swipe(0.9*x,y/2,x*0.1,y/2,500)
    def UpToDown(self):
        self.driver.swipe(x/2,y*0.4,x/2,y*0.9,500)
    def DownToUp(self):
        self.driver.swipe(x/2,y*0.9,x/2,y*0.1,500)

    #点击
    def touch(self):
        self.driver.tap([(x/2,y/2)])



    #语音长按
    def voice(self):
        try:
            __voice=self.driver.tap([(552,1548)],23000)
            print("语音发送成功")
        except Exception as err:
          assert False,\
          "语音长按失败"
        return __voice

    #鼠标长按
    def changan(self):
        print("长按运行")
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id('com.shixinyun.zuobiao:id/btn_record')
        action1.long_press(el).wait(10000).perform()

        #action2 = TouchAction(self.driver)
        #el = self.driver.find_element_by_id('XXXXX2')
       # action2.moveTo(el).release().perform()


        #TouchAction(driver).press(x, y).move_to(x, y).move_to(x, y).move_to(x, y).release().perform()