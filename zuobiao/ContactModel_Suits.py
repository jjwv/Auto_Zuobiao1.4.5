#coding:utf-8
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class ContactModel_Suits(unittest.TestCase):
    from zuobiaoCase.ContactModel import ContactModel

    ContactModel_Suits=unittest.TestSuite()
    __filename="联系人.html"
    __title="联系人测试报告"
    __description = "test1:进去管理分组添加分组" \
                    "  test2:把好友更换分组" \
                    "  test3:删除好友分组哈哈" \

    ContactModel_Suits.addTest(ContactModel("test_1"))
    ContactModel_Suits.addTest(ContactModel("test_2"))
    ContactModel_Suits.addTest(ContactModel("test_3"))


    CreateHTMLReport().HtMLReportDriver(__filename,__title,__description,ContactModel_Suits)

if  __name__=="__main__":
    unittest.main()
