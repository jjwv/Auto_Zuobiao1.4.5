'''
一、div标签文本提取
将学习视频中xpath.html文件中div标签下文本值
“第一个div” ，“第二个div” 使用xpath结构化提取并打印输出
二、ul标签文本提取
将xpath.html文件中ul标签下“流程” ，“xpath学习”，“流程2”文本值 
使用xpath结构化提取并打印输出
三、过滤标签
将xpath.html文件中的第一个div下的前3个a标签的文本及超链接
使用xpath结构化提取，打印输出
四、requests模块和lxml&xpath结合提取数据
结合上节课requests模块知识，将阳光电影网导航栏的文本及超链接结构化提取
'''
from lxml import etree
file=open('/Users/shixin/Downloads/10-lxml模块及xpath解析/10-lxml模块及xpath解析/xpath.html','r',encoding='utf-8')
html = file.read()
#print(html)  #获取的HTML
selector = etree.HTML(html)
# #获取title
# title = selector.xpath('//title/text()')[0]
# print(title)
# h1 = selector.xpath('//h1/text()')[0].strip()
# print(h1,type(h1))
# haha= selector.xpath('//div[@class="works"]/text()')
# #print(haha)
# infos=selector.xpath('//a')
# print(len(infos))
# for info in infos:
#     a_text=info.xpath('text()')[0]
#     a_href=info.xpath('@href')[0]
#     print(a_text,a_href)
'''
一、div标签文本提取
将学习视频中xpath.html文件中div标签下文本值
“第一个div” ，“第二个div” 使用xpath结构化提取并打印输出
二、ul标签文本提取
将xpath.html文件中ul标签下“流程” ，“xpath学习”，“流程2”文本值 
使用xpath结构化提取并打印输出
三、过滤标签
将xpath.html文件中的第一个div下的前3个a标签的文本及超链接
使用xpath结构化提取，打印输出
四、requests模块和lxml&xpath结合提取数据
结合上节课requests模块知识，将阳光电影网导航栏的文本及超链接结构化提取
'''
divs=selector.xpath('//div[@class="works"]/text()')
print(divs)

uls=selector.xpath('//ul/text()')
print(uls)
infos2=selector.xpath('//div[@class="works"][1]/ul[@class="title"][1]/li[position()<4]/a')
for infos2 in infos2:
    a_text = infos2.xpath('text()')[0]
    a_href=infos2.xpath('@href')[0]
    print(a_text,a_href)



