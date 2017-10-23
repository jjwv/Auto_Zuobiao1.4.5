#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Chat_Xingqing import Chat_Xingqing
from Utills.GetAppiumHelp import GetAppiumHelp


#test1：进入聊天详情页创建群组(自己是群主）
#test2：置顶和消息免打扰
#test3：查找聊天资料(安日期查找和在输入框输入哈哈哈搜索聊天资料）
#test4：查找聊天文件（图片/视频、文档、其他)
#test5：举报
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class CxingqingModel(unittest.TestCase):
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
        if a=="榴莲牛奶流沙包":
            print("手机登陆成功")
        else:
            print("手机账号登录失败")
        #点击回到消息页面
        MessagePage().Message().click()
        time.sleep(2)
        #点击联系人
        ContactPage().Contact().click()
        time.sleep(4)
        #点击我的好友分组
        ContactPage().Myfriend().click()
        time.sleep(2)
        #选择我的好友分组里的好友
        ContactPage().Friend().click()
        time.sleep(2)
        #点击红鲤鱼资料详情页发送消息
        MessagePage().SendMessage().click()
        time.sleep(1)
        #进入聊天详情页
        Chat_Xingqing().Xiaorentou().click()
        time.sleep(2)
        #点击加号添加群组聊天
        Chat_Xingqing().Add_user().click()
        time.sleep(2)
        #点击菲姐和宫雨菲非
        Chat_Xingqing().Fjie().click()
        time.sleep(1)
        Chat_Xingqing().Gfei().click()
        time.sleep(1)
        #点击确定 选择联系人后点击确定
        Chat_Xingqing().Right().click()
        time.sleep(10)

    #test2:置顶和消息免打扰
    def test_2(self):
        #点击返回到消息页面
        Chat_Xingqing().Back().click()
        time.sleep(2)
        # 进入聊天详情页
        Chat_Xingqing().Xiaorentou().click()
        time.sleep(2)
        #点击置顶
        Chat_Xingqing().Top_chat().click()
        time.sleep(2)
        #点击消息免打扰
        Chat_Xingqing().Not_disturb().click()
        time.sleep(1)
        # 点击置顶
        Chat_Xingqing().Top_chat().click()
        time.sleep(2)
        # 点击消息免打扰
        Chat_Xingqing().Not_disturb().click()
        time.sleep(1)

    #tset3：查找聊天资料
    def test_3(self):
        #点击查找聊天记录
        Chat_Xingqing().Find_chat_history().click()
        time.sleep(2)
        #定位查找聊天记录的搜索框
        Chat_Xingqing().Search_edt().send_keys("哈哈哈")
        time.sleep(3)
        #点击取消
        Chat_Xingqing().Cancel_btn().click()
        time.sleep(1)
        # 点击查找聊天记录
        Chat_Xingqing().Find_chat_history().click()
        time.sleep(2)
        #点击按日期查找
        Chat_Xingqing().Anriqi().click()
        time.sleep(2)
        #点击按日期查找返回
        Chat_Xingqing().Id_back().click()
        time.sleep(2)
        #点击取消
        Chat_Xingqing().Cancel_btn().click()
        time.sleep(1)

    #test4：查找聊天文件（搜索框搜索、图片/视频、文档、其他)
    def test_4(self):
        #定位查找聊天文件按钮
        Chat_Xingqing().Find_chat_file().click()
        time.sleep(2)
        #点击搜索框
        Chat_Xingqing().Search_layout().click()
        time.sleep(2)
        #在输入框输入哈哈，进行搜索
        Chat_Xingqing().Search_edt().send_keys("哈哈哈")
        time.sleep(1)
        #点击取消
        Chat_Xingqing().Cancel_btn().click()
        time.sleep(1)
        #点击图片/视频
        Chat_Xingqing().Picture_shipin().click()
        time.sleep(1)
        #点击文档
        Chat_Xingqing().File_s().click()
        time.sleep(1)
        #点击其他
        Chat_Xingqing().Qita().click()
        time.sleep(1)
        #点击返回
        Chat_Xingqing().Id_back().click()
        time.sleep(1)

    #点击举报
    def test_5(self):
        #点击举报
        Chat_Xingqing().Complaint_tv().click()
        time.sleep(1)
        #选择举报原因
        Chat_Xingqing().Saorao().click()
        time.sleep(1)
        Chat_Xingqing().Sqing().click()
        Chat_Xingqing().Wfa().click()
        Chat_Xingqing().Cbyy().click()
        Chat_Xingqing().Qpian().click()
        Chat_Xingqing().Mctr().click()
        time.sleep(1)
        #点击上传截图证明
        Chat_Xingqing().Iv_img().click()
        time.sleep(1)
        #点击拍照进去相机
        self.driver.tap([(524,1522)])
        #Chat_Xingqing().Zhaopai().click()
        time.sleep(2)
        #点击拍照
        self.driver.tap([(539,1788)])

        time.sleep(3)
        #点击确定
        self.driver.tap([(880,1788)])
        time.sleep(3)

        #点击上传截图
        self.driver.tap([(428,1717)])
        time.sleep(2)
        #点击照片图库
        # Chat_Xingqing().Tupintk().click()
        self.driver.tap([(500,1640)])
        time.sleep(2)
        #选取图片
        self.driver.tap([(285,1019)])
        time.sleep(2)
        #点击完成
        self.driver.tap([(950,147)])
        time.sleep(1)


        # 点击上传截图
        self.driver.tap([(653,1735)])
        time.sleep(2)
        #点击取消
        self.driver.tap([(524,1832)])
        time.sleep(2)
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击补充说明
        Chat_Xingqing().Ccsm().send_keys("哈哈哈，测试一下")
        time.sleep(1)
        #点击提交
        Chat_Xingqing().Right_tijao().click()
        time.sleep(3)
        #点击弹窗中确定
        #Chat_Xingqing().Button().click()
        time.sleep(2)



if __name__=="__main__":
    unittest.main()








