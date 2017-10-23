#cod:ing:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class SumModel_Suits(unittest.TestCase):
    from zuobiaoCase.SumModel import SumModel

    SumModel_Suits=unittest.TestSuite()
    __filename="一对一消息.html"
    __title="一对一 + 测试报告"
    __description=" test1查找好友直接发送语音"\
                    "test2:#查找好友进入聊天页面发送语音"\
                    "test3:视频通话"



    SumModel_Suits.addTest(SumModel("test_1"))
    SumModel_Suits.addTest(SumModel("test_2"))
    SumModel_Suits.addTest(SumModel("test_3"))


    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,SumModel_Suits)

if  __name__=="__main__":
    unittest.main()
