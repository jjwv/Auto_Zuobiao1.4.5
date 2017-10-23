#coding:utf-8
import smtplib
from email.mime.text import MIMEText    #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
#import sys,os
#sys.path.append(os.getcwd())
class aaa(object):
    def sendemail(self,fileName):
        #发件人
        sender = "cuiwenhaozing@163.com"
        #接件人
        receiver ="691608216@qq.com"#自己邮箱地址
        #邮件标题
        subject = '登录测试报告'
        #发件服务器
        smtpserver ='smtp.163.com'
        #登录的用户名
        username = "cuiwenhaozing@163.com"
        #登录密码
        password =  "43idonotloveyou"
        #正文消息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject#主题
        #消息正文
        text_msg = MIMEText("<html><body><p><span style='color: red'>;&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp;附件为本次回归测试报告，请各位查收!</br></p></body></html>",'html','utf-8')
        msgRoot.attach(text_msg)
        #构造附件
        #att = MIMEText(open('..TestJikeReport/+fileName', 'rb').read(), 'base64', 'utf-8')#需要更改文件路径
        att = MIMEText(open('/Users/shixin/zuobiao/Report/登录.html', 'rb').read(), 'base64', 'utf-8')  # 需要更改文件路径
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="登录.html"'
        msgRoot.attach(att)

        smtp = smtplib.SMTP_SSL()
        try:
            #站点连接
            smtp.connect(host=smtpserver,port=465)
            #登录用户
            smtp.login(username,password)
            #发送邮件（发件人、收件人、标题、正文消息、附件）
            smtp.sendmail(sender,receiver,msgRoot.as_string())
            smtp.quit()
        except Exception:
            assert False,\
                "发送失败"
