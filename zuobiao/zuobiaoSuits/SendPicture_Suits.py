#cod:ing:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class SendPicture_Suits(unittest.TestCase):
    from zuobiaoCase.SendPicture import SendPicture

    SendPicture_Suits=unittest.TestSuite()
    __filename="发送照片.html"
    __title="发送照片测试报告"
    __description="  test1:正常发送三张照片"\
                   "test2：预览后发送照片"

    SendPicture_Suits.addTest(SendPicture("test_1"))
    SendPicture_Suits.addTest(SendPicture("test_2"))


    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,SendPicture_Suits)

if  __name__=="__main__":
    unittest.main()
