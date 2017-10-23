#coding:utf-8
#封装测试套
import unittest
import sys,os
sys.path.append(os.getcwd())
from Utills.CreateHTMLReport import CreateHTMLReport
from Utills.em import _format_addr
class My_Model_Suits(unittest.TestCase):
    from zuobiaoCase.My_Model import My_Model

#声明一个测试套
    My_Model_Suits=unittest.TestSuite()
    __fileName="我的.html" #生成一个.html的测试报告文件，文件名自定义
    __title="我的模块测试报告"
    __description=  "test1:进入个人中心修改头像 " \
                    "test2:修改昵称 " \
                    "test3:二维码名片" \
                    "test4:更改性别" \
                    "test5:更改生日  " \
                    "test6：更改地区" \
                    "test7:工作信息(行业，公司，职位）"\
                    "test8:更改电话"\
                    "test9:更改邮箱"


# #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    My_Model_Suits.addTest(My_Model("test_1"))
    My_Model_Suits.addTest(My_Model("test_2"))
    My_Model_Suits.addTest(My_Model("test_3"))
    My_Model_Suits.addTest(My_Model("test_4"))
    My_Model_Suits.addTest(My_Model("test_5"))
    My_Model_Suits.addTest(My_Model("test_6"))
    My_Model_Suits.addTest(My_Model("test_7"))
    My_Model_Suits.addTest(My_Model("test_8"))
    My_Model_Suits.addTest(My_Model("test_9"))



    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,My_Model_Suits)
if __name__=="__main__":
    unittest.main()
    em = _format_addr()

