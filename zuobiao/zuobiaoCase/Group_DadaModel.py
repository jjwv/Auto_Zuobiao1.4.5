#coding:utf-8
from Utills.GetAppiumDriver import GetAppiumDriver
from CommonFunction.LoginPage import LoginPage
from CommonFunction.MyPage import MyPage
from CommonFunction.MessagePage import MessagePage
from CommonFunction.ContactsPage import ContactPage
from CommonFunction.Group_Data import Group_Data
from Utills.GetAppiumHelp import GetAppiumHelp


#test1：群主或管理员更改群头性  (拍照和相册选择）
#test2:群主或管理员邀请成员
#test3：群主或管理员移除成员
#test4:群主及管理员修改群成员（我的名片）
#test5:修改群聊名称
#test6: 分享群二维码
#test7:群公告
#test8：更改自己的群名牌
#test9:点击入群验证 聊天置顶及消息免打扰
import time
import unittest
import sys,os
sys.path.append(os.getcwd())
class Group_DataModel(unittest.TestCase):
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
        time.sleep(3)
        #点击群头像
        Group_Data().Group_head().click()
        time.sleep(1)
        #点击左上。。。
        #self.driver.tap([(983,172)])
        #time.sleep(1)
        # 长按出现换头像菜单
        self.driver.tap([(200, 1000)], 1000)
        time.sleep(1)
        # 点击从相册选择
        # My_Headpage().Cong_Xz().click()
        self.driver.tap([(460, 1479)])
        time.sleep(1)
        #点击拍照
        self.driver.tap([(533,1484)])
        time.sleep(2)
        #点击拍照按钮
        self.driver.tap([(544,1790)])
        time.sleep(4)
        #点击确定
        self.driver.tap([(872,1793)])
        time.sleep(3)
        #点击完成
        self.driver.tap([(831,173)])
        time.sleep(8)


        # 点击群头像  相册选取图片中作为群头像
        Group_Data().Group_head().click()
        time.sleep(1)
        # 长按出现换头像菜单
        self.driver.tap([(200, 1000)], 1000)
        time.sleep(1)
        self.driver.tap([(522, 1649)])
        time.sleep(1)
        #点击从相册选择
        self.driver.tap([(436,794)])
        time.sleep(1)
        self.driver.tap([(682,360)])
        time.sleep(1)

        #点击完成
        self.driver.tap([(821,142)])
        time.sleep(7)

    #test2:群主或管理员邀请成员
    def test_2(self):
        #点击群成员
        time.sleep(1)
        Group_Data().Group_member().click()
        time.sleep(1)
        #点击。。。
        Group_Data().Right().click()
        time.sleep(1)
        #点击邀请成员
        self.driver.tap([(505,1498)])
        time.sleep(1)
        #点击红鲤鱼
        Group_Data().Hongliyu().click()
        time.sleep(3)
        #点击确定
        Group_Data().Right().click()
        time.sleep(1)

    #test3：群主或管理员移除成员
    def test_3(self):

        # 点击。。。
        Group_Data().Right().click()
        time.sleep(1)
        # 点击移除成员
        self.driver.tap([(520,1685)])
        time.sleep(1)
        #向下滑屏
        #GetAppiumHelp().DownToUp()
        time.sleep(1)
        # 点击红鲤鱼
        Group_Data().Hongliyu().click()
        time.sleep(1)
        # 点击删除
        Group_Data().Right().click()
        time.sleep(1)
        #点击弹窗中的确定
        Group_Data().Qud().click()
        time.sleep(4)
        #点击返回
        Group_Data().Back().click()
        time.sleep(1)

    #test4:群主及管理员修改群成员（我的名片）
    def test_4(self):
        #点击群成员
        Group_Data().Group_member().click()
        time.sleep(1)
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击一个群成员 万水千山总是情
        ContactPage().Wanshui().click()
        time.sleep(1)
        #点击群名片
        Group_Data().Member_name().click()
        time.sleep(1)
        #在编辑群名片页中改名片
        Group_Data().Member_et().send_keys("123")
        time.sleep(2)
        #点击完成
        Group_Data().Right().click()
        time.sleep(5)
        # 点击我的群名片
        Group_Data().Member_name().click()
        time.sleep(1)
        # 在编辑群名片页中改名片
        Group_Data().Member_et().clear()
        time.sleep(1)
        Group_Data().Member_et().send_keys("万水千山总是情")
        # 点击完成
        Group_Data().Right().click()
        time.sleep(5)
        #点击返回
        Group_Data().Back().click()
        time.sleep(1)
        # 点击返回 回到群资料
        Group_Data().Back().click()
        time.sleep(1)

    # test5:修改群聊名称
    def test_5(self):
        #点击群聊名称
        Group_Data().Qlmc().click()
        time.sleep(1)
        #在群聊名称中修改名称
        Group_Data().Qlmc_Srk().send_keys("哈哈哈")
        time.sleep(1)
        #点击完成
        Group_Data().Right().click()
        time.sleep(5)
        # 点击群聊名称
        Group_Data().Qlmc().click()
        time.sleep(1)
        # 在群聊名称中修改名称
        Group_Data().Qlmc_Srk().send_keys("鬼啦啦啦啦")
        time.sleep(1)
        # 点击完成
        Group_Data().Right().click()
        time.sleep(5)

    # test6: 分享群二维码
    def test_6(self):
        #点击群二维码
        self.driver.tap([(662,953)])
        time.sleep(1)
        #点击保存到手机
        Group_Data().Save_to_mobile().click()
        time.sleep(1)
        #点击分享
        Group_Data().Share_qr().click()
        time.sleep(1)
        #向左滑屏
        GetAppiumHelp().RightToLeft()
        time.sleep(1)
        GetAppiumHelp().RightToLeft()
        time.sleep(1)

        #self.driver.swipe(530,1680,557,750,1000)
        #time.sleep(1)
        #点击一起开黑
        ContactPage().Yqkh().click()
        time.sleep(1)
        #点击发送
        Group_Data().Right().click()
        time.sleep(1)
        #点击返回群资料
        Group_Data().Back().click()
        time.sleep(1)

    # test7:群公告
    def test_7(self):
        #点击群公告
        Group_Data().Group_notice().click()
        time.sleep(1)
        #点击编辑
        Group_Data().Right().click()
        time.sleep(1)
        #点击群公告中输入框
        Group_Data().Group_content().send_keys("啦啦啦该怎么办啊")
        time.sleep(1)
        #点击发布
        Group_Data().Right().click()
        time.sleep(5)
        #回到群资料

    #test8：更改自己的群名牌
    def test_8(self):
        #点击我的群名牌
        Group_Data().Group_my_nickname().click()
        time.sleep(2)
        #点击编辑群名片
        Group_Data().Member_name_et().send_keys("哒哒哒哒哒哒哒哒")
        time.sleep(2)
        #点击完成
        Group_Data().Right().click()
        time.sleep(5)

    #test9:点击入群验证 聊天置顶及消息免打扰
    def test_9(self):
        #向上滑屏
        GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击去群验证
        Group_Data().Group_validate().click()
        time.sleep(1)
        # 点击置顶
        Group_Data().Chat_on_top().click()
        time.sleep(2)
        # 点击消息免打扰
        Group_Data().Message_no_disturb().click()
        time.sleep(1)

    # test10:查找聊天记录
    '''def test_10(self):
        #GetAppiumHelp().DownToUp()
        time.sleep(1)
        #点击查找聊天记录
        Group_Data().Find_chat_history().click()
        time.sleep(1)
        #点击按成员查找
        self.driver.tap([(266,552)])
        time.sleep(1)
        #在输入框搜索红鲤鱼
        Group_Data().Qsqk().send_keys("红鲤鱼与绿鲤鱼与驴")
        time.sleep(1)
        #点击红鲤鱼
        ContactPage().Friend().click()
        time.sleep(1)
        #点击返回
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

    #test11:查找聊天文件（图片/视频、文档、其他)
    def test_11(self):
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

    #test12：举报
    def test_12(self):
        #GetAppiumHelp().DownToUp()
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
        # 点击弹窗中确定
        Group_Data().Qud().click()
        time.sleep(2)'''








if __name__=="__main__":
    unittest.main()




