from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "cuiwenhaozing@163.com"
password = "43idonotloveyou"
to_addr ="xianglei@shixinyun.com","691608216@qq.com","jiangzhiqiang@shixinyun.com","gongyufei@shixinyun.com","zhangxuzhou@shixinyun.com","jiangwenhong@shixinyun.com","zengxiaoxue@shixinyun.com","fanshaohua@shixinyun.com","mayuanqi@shixinyun.com"
smtp_server = "smtp.163.com"

msg = MIMEMultipart()
#msg = MIMEText('测试报告', 'plain', 'utf-8')#内容
msg['From'] = _format_addr('崔文豪 <%s>' % from_addr)#发件人
msg['To'] = _format_addr('Test <%s>' % [to_addr])
msg['Subject'] = Header('群组详情页2测试报告', 'utf-8').encode()#主题

# 邮件正文是MIMEText:
msg.attach(MIMEText('测试报告见附件', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/shixin/zuobiao/Report/群组详情页2.html', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'html', filename='群组详情页2')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='群组详情页2.html')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()