#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class Miliao_Suits(unittest.TestCase):
    from zuobiaoCase.Miliao_Model import Miliao #放在class下面，不然会执行完001，最后一条case又会重新执行一遍



#声明一个测试套
    Miliao_Suits=unittest.TestSuite()
    __fileName="密聊.html" #生成一个.html的测试报告文件，文件名自定义
    __title="密聊测试报告"
    __description="test1: 点击红鲤鱼进行密聊发照片" \
                "test2:发送密聊文本信息" \
                "test3：发送表情" \
                "test4:全局搜索密聊" \



#第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Miliao_Suits.addTest(Miliao('test_1'))
    Miliao_Suits.addTest(Miliao('test_2'))
    Miliao_Suits.addTest(Miliao('test_3'))
    Miliao_Suits.addTest(Miliao('test_4'))

    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Miliao_Suits)
if __name__=="__main__":
    unittest.main()