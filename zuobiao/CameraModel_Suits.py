#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class CameraModel_Suits(unittest.TestCase):
    from zuobiaoCase.CameraModel import CameraModel#放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    CameraModel_Suits=unittest.TestSuite()
    __fileName="相机.html" #生成一个.html的测试报告文件，文件名自定义
    __title="相机按钮测试报告"
    __description=      "test1:点击长按正常发送和取消小视频"\
                        "  test2:长按录制小视频后点击✘取消"\
                        "  test3:点击一下进行拍照发送"\
                        "  test4:点击一下进行拍照取消"\
                        "  test5:点击转换前置摄像头进行录像"\
                        "  test6:点击转换前置摄像头进行拍照"
     #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化
    CameraModel_Suits.addTest(CameraModel('test_1'))
    CameraModel_Suits.addTest(CameraModel('test_2'))
    CameraModel_Suits.addTest(CameraModel('test_3'))
    CameraModel_Suits.addTest(CameraModel('test_4'))
    CameraModel_Suits.addTest(CameraModel('test_5'))
    CameraModel_Suits.addTest(CameraModel('test_6'))
    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,CameraModel_Suits)
if __name__=="__main__":
    unittest.main()


