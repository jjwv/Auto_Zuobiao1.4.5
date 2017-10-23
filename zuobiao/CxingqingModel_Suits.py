#coding:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class CxingqingModel_Suits(unittest.TestCase):
    from zuobiaoCase.CxingqingModel import CxingqingModel

    CxingqingModel_Suits=unittest.TestSuite()
    __filename="聊天详情.html"
    __title="聊天详情测试报告"
    __description=" test1：进入聊天详情页创建群组(自己是群主"\
                    "test2：置顶和消息免打扰"\
                    "test3：查找聊天资料(安日期查找和在输入框输入哈哈哈搜索聊天资料）"\
                    "test4：查找聊天文件（图片/视频、文档、其他)"\
                    "test5：举报"

    CxingqingModel_Suits.addTest(CxingqingModel("test_1"))
    CxingqingModel_Suits.addTest(CxingqingModel("test_2"))
    CxingqingModel_Suits.addTest(CxingqingModel("test_3"))
    CxingqingModel_Suits.addTest(CxingqingModel("test_4"))
    CxingqingModel_Suits.addTest(CxingqingModel("test_5"))

    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,CxingqingModel_Suits)

if  __name__=="__main__":
    unittest.main()