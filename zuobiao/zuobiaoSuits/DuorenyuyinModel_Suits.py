# 封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class Duorenyuyin_Suits(unittest.TestCase):
    from zuobiaoCase.DuorenyuyinModel import Duorenyuyin_Model  # 放在class下面，不然会执行完001，最后一条case又会重新执行一遍

    # 声明一个测试套
    Duorenyuyin_Suits = unittest.TestSuite()
    __fileName = "多人语音.html"  # 生成一个.html的测试报告文件，文件名自定义
    __title = "测试报告多人语音"
    __description = "test1：创建多人语音" \
                    "test2:多人语音界面按键操作" \
                    "test3：添加8人创建多人语音" \
                    "test4:创建多人语音然后逐渐添加用户" \


        # 第一种方法，推荐多条case用：
    # 添加用例到测试套，相当于类的实例化
    Duorenyuyin_Suits.addTest(Duorenyuyin_Model('test_1'))
    Duorenyuyin_Suits.addTest(Duorenyuyin_Model('test_2'))
    Duorenyuyin_Suits.addTest(Duorenyuyin_Model('test_3'))
    Duorenyuyin_Suits.addTest(Duorenyuyin_Model('test_4'))


    # loginSuit.addTest(LoginModule('testlogin002'))
    #     #执行测试
    # unittest.TextTestRunner().run(loginSuit)
    # 一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName, __title, __description,Duorenyuyin_Suits)


if __name__ == "__main__":
    unittest.main()