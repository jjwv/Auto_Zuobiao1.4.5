#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
from Utills.em import _format_addr
class LoginSuit(unittest.TestCase):
    from zuobiaoCase.LoginModel import LoginModel #放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    loginSuit=unittest.TestSuite()
    __fileName="登录.html" #生成一个.html的测试报告文件，文件名自定义
    __title="登录测试报告"
    __description="case1手机登录  case2邮箱登录"
# #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    loginSuit.addTest(LoginModel('test_login'))
    loginSuit.addTest(LoginModel('test_email'))
    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,loginSuit)
if __name__=="__main__":
    unittest.main()



























# #声明一个测试套
#     loginSuit=unittest.TestSuite()
# #第一种方法，推荐多条case用：
#     #添加用例到测试套，相当于类的实例化
#     loginSuit.addTest(LoginModule('testlogin001'))
#     loginSuit.addTest(RegstModule('testRegs001'))
#     loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
#     unittest.TextTestRunner().run(loginSuit)
# if __name__=='__mian__':
#     unittest.main()
#
#第二种方法,适用于case少的问题
#     # 声明一个列表
#     logincaseList=("testlogin001","testlogin002","testRegs001")
#     # 把列表中的值放入测试套
#     for tmp in logincaseList:
#         loginSuit.addTest(LoginModule(tmp))
#     # 执行测试套
#     unittest.TextTestRunner().run(loginSuit)
# if __name__=='__main__':
#     unittest.main()
