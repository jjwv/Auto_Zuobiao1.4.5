#coding:utf-8
import unittest,requests

class Auto(unittest.TestCase):
    def setUp(self):
        r = requests.post(url='http://114.112.101.156:8080/manager/user/destroy?token=zbadmin@2017&mobile=18301106522')  # 最基本的GET请求
        print(r.status_code)  # 获取返回状态
        #r = requests.post(url='http://114.112.101.156:8080/manager/user/destroy', params={"token=zbadmin@2017，mobile=18301106522"})  # 带参数的GET请求
        print(r.url)
        print(r.text)  # 打印解码后的返回数据

