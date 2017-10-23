#coding:utf-8
#封装测试套
import unittest
import sys,os
sys.path.append(os.getcwd())
from Utills.CreateHTMLReport import CreateHTMLReport
class Group_DataModeltwoSuits(unittest.TestCase):
    from zuobiaoCase.Group_DataModeltwo import Group_DataModeltwo
#声明一个测试套
    Group_DadaModeltwoSuits=unittest.TestSuite()
    __fileName="群组详情页2.html" #生成一个.html的测试报告文件，文件名自定义
    __title="群组详情页测试报告"
    __description="test1:群资料       查找聊天文件（图片/视频、文档、其他) " \
                  "test2:群资料        举报 " \
                  "test3:群主设置管理员" \
                  "test4: 群主     设为群主" \
                  "test5:群公告   " \
                  "test6：清空聊天记录" \


# #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_1'))
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_2'))
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_3'))
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_4'))
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_5'))
    Group_DadaModeltwoSuits.addTest(Group_DataModeltwo('test_6'))


    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Group_DadaModeltwoSuits)
if __name__=="__main__":
    unittest.main()



