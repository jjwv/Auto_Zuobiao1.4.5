#coding:utf-8
#封装测试套
import unittest
import sys,os
sys.path.append(os.getcwd())
from Utills.CreateHTMLReport import CreateHTMLReport
class Group_DataModelSuits(unittest.TestCase):
    from zuobiaoCase.Group_DadaModel import Group_DataModel
#声明一个测试套
    Group_DadaModelSuits=unittest.TestSuite()
    __fileName="群组详情页1.html" #生成一个.html的测试报告文件，文件名自定义
    __title="群组详情页测试报告"
    __description="test1：群主或管理员更改群头性  (拍照和相册选择）" \
                  "test2:群主或管理员邀请成员   test3：群主或管理员移除成员  " \
                  "test4:群主及管理员修改群成员（我的名片)  " \
                  "test5:修改群聊名称   " \
                  "test6: 分享群二维码   " \
                  "test7:群公告   " \
                  "test8：更改自己的群名牌  " \
                  "test9:点击入群验证 聊天置顶及消息免打扰"

# #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Group_DadaModelSuits.addTest(Group_DataModel('test_1'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_2'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_3'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_4'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_5'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_6'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_7'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_8'))
    Group_DadaModelSuits.addTest(Group_DataModel('test_9'))

    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Group_DadaModelSuits)
if __name__=="__main__":
    unittest.main()

