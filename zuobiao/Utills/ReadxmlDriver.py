#导入读取xml文件的minidom模块

# #coding:utf-8
from xml.dom import minidom
import sys,os
sys.path.append(os.getcwd())
class ReadxmlDriver(object):
    def retrunXmlFile(self,fileName,fistNode,secondNode):#传递参数
        #打开xml文件，通过相对路径，parse:打开，两种不同类型用+连接,变量fileName代替文件名,这里是公用模块，不能写死文件名不便于操作
        rootfile=minidom.parse("../TestShereData/"+fileName)
        #获取文件的一级标签，fistNode代表一级标签名称，该文件中有可能有多个一级标签，不能写死，用变量代替[]中的0是标签的小角标，默认为0
        OneNode=rootfile.getElementsByTagName(fistNode)[0]
        #获取文件的二级标签
        twoNode=OneNode.getElementsByTagName(secondNode)[0].childNodes[0].nodeValue
        return twoNode