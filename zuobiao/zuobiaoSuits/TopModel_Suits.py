#cod:ing:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class TopModel_Suits(unittest.TestCase):
    from zuobiaoCase.TopModel import TopModel

    TopModel_Suits=unittest.TestSuite()
    __filename="坐标顶端功能.html"
    __title="坐标顶端功能测试报告"
    __description=" test1：点击放大镜进行搜索框搜索"\
                    "test2:点击放大镜进行按联系人 聊天记录 文件进行搜索"\
                    "test3：点击铃铛查看验证消息"\
                    "test4:加号点击创建群组后解散"\
                    "test5：加号点添加联系人"\
                    "test6:加号点扫一扫"



    TopModel_Suits.addTest(TopModel("test_1"))
    TopModel_Suits.addTest(TopModel("test_2"))
    TopModel_Suits.addTest(TopModel("test_3"))
    TopModel_Suits.addTest(TopModel("test_4"))
    TopModel_Suits.addTest(TopModel("test_5"))
    TopModel_Suits.addTest(TopModel("test_6"))


    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,TopModel_Suits)

if  __name__=="__main__":
    unittest.main()
