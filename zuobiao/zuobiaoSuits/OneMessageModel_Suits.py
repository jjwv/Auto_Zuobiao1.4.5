#cod:ing:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class OneMessageModel_Suits(unittest.TestCase):
    from zuobiaoCase.OneMessageModel import OneMessageModel

    OneMessageModel_Suits=unittest.TestSuite()
    __filename="消息一对一.html"
    __title="消息一对一 发送消息及语音测试报告"
    __description="  test1：发送文字消息及语音消息"\
                    "test2：发送语音消息松开试听"\
                    "test3:发送语音消息松开试听取消"\
                    "test4:发送语音然后左划删除"

    OneMessageModel_Suits.addTest(OneMessageModel("test_1"))
    OneMessageModel_Suits.addTest(OneMessageModel("test_2"))
    OneMessageModel_Suits.addTest(OneMessageModel("test_3"))
    OneMessageModel_Suits.addTest(OneMessageModel("test_4"))

    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,OneMessageModel_Suits)

if  __name__=="__main__":
    unittest.main()
