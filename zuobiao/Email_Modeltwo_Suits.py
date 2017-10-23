#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class Email_Modeltwo_suit(unittest.TestCase):
    from zuobiaoCase.Email_Modeltwo import Email_Modeltwo#放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    Email_Modeltwo_suit=unittest.TestSuite()
    __fileName="邮件2.html" #生成一个.html的测试报告文件，文件名自定义
    __title="邮件测试报告2"
    __description="test1：添加第二个账号" \
                "test2:发送多个收件地址的邮件" \
                "test3：发送多个抄送地址的邮件" \
                "test4:点击title添加账号" \
                "test5:转发"\
                "test6:回复" \
                "test7:全部回复"\





#第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_1'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_2'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_3'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_4'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_5'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_6'))
    Email_Modeltwo_suit.addTest(Email_Modeltwo('test_7'))

    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Email_Modeltwo_suit)
if __name__=="__main__":
    unittest.main()