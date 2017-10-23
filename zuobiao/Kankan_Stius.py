#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport

class Kankan_Suit(unittest.TestCase):
    from zuobiaoCase.Kankan_Model import Kankan_Model #放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    Kankan_Suit=unittest.TestSuite()
    __fileName="看看.html" #生成一个.html的测试报告文件，文件名自定义
    __title="看看测试报告"
    __description="test1：看看换一批" \



#第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Kankan_Suit.addTest(Kankan_Model('test_1'))

    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Kankan_Suit)
if __name__=="__main__":
    unittest.main()