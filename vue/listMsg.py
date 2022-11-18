#!C:\Users\B24\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import cgi
import guestbook as gb
import json
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
msgList=gb.getList()

ret=[]
for (id,title, msg, nick, likes) in msgList:
	ret.append({
        "id": id,
        "title": title,
        "likes": likes
    })

print(json.dumps(ret))
