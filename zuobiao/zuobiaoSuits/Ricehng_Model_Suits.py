#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class Richeng_Model_Suit(unittest.TestCase):
    from zuobiaoCase.Richeng_Model import Richeng_Model #放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    Richeng_Model_Suit=unittest.TestSuite()
    __fileName="日程.html" #生成一个.html的测试报告文件，文件名自定义
    __title="日程测试报告"
    __description="test1：创建日程" \
                "test2:创建多个日程，有提醒" \
                "test3：取消日程" \
                "test4:删除日程" \
                "test5:搜索日程"\
                "test6:下滑选择当天以前的日期创建日程" \
                "test7:选择跨月份的日期创建日程"


#第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Richeng_Model_Suit.addTest(Richeng_Model('test_1'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_2'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_3'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_4'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_5'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_6'))
    Richeng_Model_Suit.addTest(Richeng_Model('test_7'))
    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Richeng_Model_Suit)
if __name__=="__main__":
    unittest.main()