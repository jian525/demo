#!C:\Users\ASUS\AppData\Local\Programs\Python\Python310\python.exe
# print headers first
import msgModel
import cgi
from datetime import date, datetime
import json
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")


def genList():
    jsonStr = form.getvalue('dat')
    dat = json.loads(jsonStr)
    msgList = msgModel.getList()  # get an array from model
    result = {
        "dat": dat,
        "list": msgList
    }
    return (result)


def likeit(xid):
    msgModel.like(xid)


# main starts here
form = cgi.FieldStorage()

try:
    act = form.getvalue('o')
except:
    #print("o missing")
    exit()

para = ()
# we can start accessing DB now
if act == 'g':  # get one record by xid
    result = genList()
    print(json.dumps(result, ensure_ascii=True))  # dump json string to client
# elif act == 'like':
   # mid = int(form.getvalue('id'))
    # likeit(mid)
elif act == 'add':
    mid = int(form.getvalue('id'))
    msgModel.add(mid)
elif act == 'del':
    mid = int(form.getvalue('id'))
    msgModel.kill(mid)
