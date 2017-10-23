#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class Email_Model_suit(unittest.TestCase):
    from zuobiaoCase.Email_Model import Email_Model#放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    Email_Model_suit=unittest.TestSuite()
    __fileName="邮件1.html" #生成一个.html的测试报告文件，文件名自定义
    __title="邮件测试报告1"
    __description="test1：进入邮箱添加邮箱账号  错误邮箱账号正确密码" \
                "test2:添加正确的邮箱账号和错误密码" \
                "test3：添加正确的账号和密码" \
                "test4:发送邮件  输入错误邮箱地址 有主题" \
                "test5:输入正确收件人地址，不输入主题"\
                "test6:输入正确邮箱地址，不输入主题，发送邮件" \
                "test7:存入草稿箱"\
                "test_8:进入草稿箱，发送草稿"  \
                "test9:查看已发送，然后删除账号"




#第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    Email_Model_suit.addTest(Email_Model('test_1'))
    Email_Model_suit.addTest(Email_Model('test_2'))
    Email_Model_suit.addTest(Email_Model('test_3'))
    Email_Model_suit.addTest(Email_Model('test_4'))
    Email_Model_suit.addTest(Email_Model('test_5'))
    Email_Model_suit.addTest(Email_Model('test_6'))
    Email_Model_suit.addTest(Email_Model('test_7'))
    Email_Model_suit.addTest(Email_Model('test_8'))
    Email_Model_suit.addTest(Email_Model('test_9'))
    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,Email_Model_suit)
if __name__=="__main__":
    unittest.main()