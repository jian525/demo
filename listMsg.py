#!C:\Users\ASUS\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: utf-8 -*-
# 處理stdio輸出編碼，以避免亂碼
import guestbook as gb
from dbConfig import conn, cur
import cgi
import codecs
import sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

# 連線DB
#import guestbook as gb
# 先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Guestbook: ListMsg</title>
</head>
<body>
倉庫 <a href='addMsgForm.html'> 新增商品 </a> <a href='main.html'> 返回首頁 </a><hr>
""")
msgList = gb.getList()
# 查詢
'''
sql="select id, title,msg, nickname,likes from guestbook order by likes desc;"
cur.execute(sql)
records = cur.fetchall()
'''
for (id, title, nick, msg) in msgList:
    print(f"<p>編號{id}:  商品:{title} 價錢:{nick} 數量:{msg} </p>")

print("</body></html>")
