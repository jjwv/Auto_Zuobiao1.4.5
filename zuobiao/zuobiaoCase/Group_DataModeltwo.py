#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Group_Data import Group_Data
from Utills.GetAppiumHelp import GetAppiumHelp

#test1:群资料   查找聊天记录
#test2: 群资料       查找聊天文件（图片/视频、文档、其他)
#test3： 群资料        举报
#test4：群主设置管理员
#test5：群主     设为群主
#test6: 清空聊天记录
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class Group_DataModeltwo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=GetAppiumDriver().driver

    def setUp(self):
        pass

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        cls.driver=GetAppiumDriver().driver
        cls.driver.quit()

    # test1:查找聊天记录
    def test_1(self):
        time.sleep(3)
        # 点击浮层
        LoginPage().fuceng().click()
        time.sleep(2)
        #输入账号
        LoginPage().zhanghao().send_keys("13691515688")
        #输入密码
        time.sleep(3)
        LoginPage().password().send_keys("123456")
        #点击登录
        time.sleep(3)
        LoginPage().login_btn().click()
        time.sleep(4)
        #点击关闭新手指导
        LoginPage().close_xin().click()
        time.sleep(2)
        #点击到我的进去我的页面
        MyPage().MyBtn().click()
        #获取title
        a=MyPage().text1().text
        if a=="打个鸡没问题":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
        # 点击回到消息页面
        MessagePage().Message().click()
        time.sleep(2)
        # 点击联系人
        ContactPage().Contact().click()
        time.sleep(2)

        time.sleep(1)
        #右划到群
        GetAppiumHelp().RightToLeft()
        time.sleep(2)
        GetAppiumHelp().UpToDown()
        time.sleep(2)
        #点击鬼拉拉群  自己是群主
        self.driver.tap([(422,683)])
        time.sleep(1)
        #点击小人头进入群资料
        self.driver.tap([(983,157)])
        time.sleep(2)
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        # 点击查找聊天记录
        Group_Data().Find_chat_history().click()
        time.sleep(1)
        # 点击按成员查找
        self.driver.tap([(266, 552)])
        time.sleep(1)
        # 在输入框搜索红鲤鱼
        Group_Data().Qsqk().send_keys("红鲤鱼与绿鲤鱼与驴")
        time.sleep(1)
        # 点击红鲤鱼
        ContactPage().Friend().click()
        time.sleep(1)
        # 点击返回
        Group_Data().Back().click()
        time.sleep(1)

        #点击按日期查找
        self.driver.tap([(809,551)])
        time.sleep(1)
        #点击返回
        Group_Data().Back().click()
        time.sleep(1)
        #点击取消
        Group_Data().Cancel_btn().click()
        time.sleep(1)

    #test2:查找聊天文件（图片/视频、文档、其他)
    def test_2(self):
        #GetAppiumHelp().DownToUp()
        time.sleep(1)
        #定位查找聊天文件按钮
        Group_Data().Find_chat_file().click()
        time.sleep(2)
        #点击搜索框
        Group_Data().Search_layout().click()
        time.sleep(2)
        #在输入框输入哈哈，进行搜索
        Group_Data().Search_edt().send_keys("哈哈哈")
        time.sleep(1)
        #点击取消
        Group_Data().Cancel_btn().click()
        time.sleep(1)
        #点击图片/视频
        Group_Data().Picture_shipin().click()
        time.sleep(1)
        #点击文档
        Group_Data().File_s().click()
        time.sleep(1)
        #点击其他
        Group_Data().Qita().click()
        time.sleep(1)
        #点击返回
        Group_Data().Back().click()
        time.sleep(1)

    #test3：群主设置管理员
    def test_3(self):
        #向上滑屏
        GetAppiumHelp().UpToDown()
        time.sleep(1)
        #点击群成员
        Group_Data().Group_member().click()
        time.sleep(1)
        #GetAppiumHelp().UpToDown()
        time.sleep(1)
        #点击阿老范
        ContactPage().LF().click()
        time.sleep(1)
        #点击设为管理员
        Group_Data().Guanliyuan().click()
        time.sleep(1)
        #点击浮窗页的确定
        #Group_Data().Qud().click()
        time.sleep(1)

     #test4：群主     设为群主
    def test_4(self):
        # 点击群成员
        #Group_Data().Group_member().click()
        #time.sleep(1)
        # 点击。。。
        #Group_Data().Right().click()
        #time.sleep(1)
        # 点击邀请成员
        #self.driver.tap([(505, 1498)])
        time.sleep(1)
        # 点击宫雨菲非
        Group_Data().Gongyuff().click()
        time.sleep(1)
        #点击设为群主
        Group_Data().Shequnzhu().click()
        time.sleep(1)
        #谈窗页点击取消
        Group_Data().Quxiao().click()
        time.sleep(1)
        #点击返回
        Group_Data().Back().click()
        time.sleep(1)
        Group_Data().Back().click()
        time.sleep(1)

    #test5: 清空聊天记录
    def test_5(self):
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击清空聊天记录
        Group_Data().Clear_chat().click()
        time.sleep(1)
        #点击清空聊天记录
        #Group_Data().Qud().click()
        Group_Data().qingkongjl().click()

    #test6:举报
    def test_6(self):
        # GetAppiumHelp().DownToUp()
        time.sleep(1)
        # 点击举报
        Group_Data().Complaint_tv().click()
        time.sleep(1)
        # 选择举报原因
        Group_Data().Saorao().click()
        time.sleep(1)
        Group_Data().Sqing().click()
        Group_Data().Wfa().click()
        Group_Data().Cbyy().click()
        Group_Data().Qpian().click()
        Group_Data().Mctr().click()
        time.sleep(1)
        # 点击上传截图证明
        Group_Data().Iv_img().click()
        time.sleep(1)
        # 点击拍照进去相机
        self.driver.tap([(524, 1522)])
        time.sleep(2)
        # 点击拍照
        self.driver.tap([(539, 1788)])
        time.sleep(3)
        # 点击确定
        self.driver.tap([(880, 1788)])
        time.sleep(3)

        # 点击上传截图
        self.driver.tap([(428, 1717)])
        time.sleep(2)
        # 点击照片图库
        self.driver.tap([(524, 1653)])
        time.sleep(2)
        # 选取图片
        self.driver.tap([(285, 1019)])
        time.sleep(2)
        # 点击完成
        self.driver.tap([(950, 147)])
        time.sleep(1)

        # 点击上传截图
        self.driver.tap([(653, 1735)])
        time.sleep(2)
        # 点击取消
        self.driver.tap([(524, 1832)])
        time.sleep(2)
        # 向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        # 点击补充说明
        Group_Data().Ccsm().send_keys("哈哈哈，测试一下")
        time.sleep(1)
        # 点击提交
        Group_Data().Right().click()
        time.sleep(5)
        # # 点击弹窗中确定
        # Group_Data().Qud().click()
        # time.sleep(4)






if __name__=="__main__":
    unittest.main()
