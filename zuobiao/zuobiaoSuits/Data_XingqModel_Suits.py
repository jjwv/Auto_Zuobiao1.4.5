#coding:utf-8
import unittest
import sys,os
sys.path.append(os.getcwd())
from Utills.CreateHTMLReport import CreateHTMLReport
class Data_XingqModel_Suits(unittest.TestCase):
    from zuobiaoCase.Data_XingqModel import Data_XingqModel

    Data_XingqModel_Suits=unittest.TestSuite()
    __filename="资料详情.html"
    __title="资料详情页测试报告"
    __description="test1:给响雷更改备注还原备注"\
                    "test2:点击查看工作信息"\
                    "test3:点击。。。进行举报删除联系人"\
                    "test4：点击。。。举报  "

    Data_XingqModel_Suits.addTest(Data_XingqModel("test_1"))
    Data_XingqModel_Suits.addTest(Data_XingqModel("test_2"))
    Data_XingqModel_Suits.addTest(Data_XingqModel("test_3"))
    Data_XingqModel_Suits.addTest(Data_XingqModel("test_4"))

    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,Data_XingqModel_Suits)

if  __name__=="__main__":
    unittest.main()
