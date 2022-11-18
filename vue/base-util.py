#!C:\Program Files\Python310\python.exe
#print headers first
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")

import json
import cgi
from dbConfig import conn, cur

def getRecord():
	try:
		xid=int(form.getvalue('i'))
	except:
		exit()


	sql=f"select {fDBList} from {tableNm} where xid= {xid};"
	cur.execute(sql)

	record = cur.fetchone()
	result={}
	if record:
		L=len(record)
	else:
		L=0

	for i in range(0,len(fFMList)):
		o=record[i]
		if isinstance(o, datetime):
			o=o.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(o, date):
			o=o.strftime('%Y-%m-%d')

		result[fFMList[i]] = o
	print(json.dumps(result))

def setRecord():
	#load the posted data
	try:
		xid=int(form.getvalue('i'))
		str=form.getvalue('dat')
		dat = json.loads(str)
	except:
		exit()

	if xid<0: #insert
		#sql = f"insert into `{tableNm}` ( {fDBList}, group_memb) values ({paraList}, (select max(group_memb)+1 from `{tableNm}` a where group_no={GRP_NO}));"
		sql = f"insert into `base` ( {fDBList} ) values ({paraList});"
		#print(sql)
		cur.execute(sql,tuple(valList))
		print('{"msg":"OK"}')
	else: #update
		#get the data before update and save to baselog
		sql=f"select * from `base` where xid={xid}"
		cur.execute(sql)
		rec=cur.fetchone()
		temp={}
		field_names = [i[0] for i in cur.description]
		i=0

		if temp:
			jsonStr=json.dumps(temp,ensure_ascii=False)
			sql = "insert into `baselog` ( xid, json) values (%s, %s);"
			cur.execute(sql,(xid,jsonStr))
		#find new zipno with zipcodetw
			
		#now get to update
		sql = f"update `base` set {updList} where xid={xid};"
		cur.execute(sql,tuple(valList))
		print('{"msg":"OK"}')
	conn.commit()
	conn.close()

def findRecords():
	try:
		str=form.getvalue('q') #get query strings in json
		qStrs = json.loads(str)
	except:
		exit()
		pass

	if page==0:
		sql=f"select count(*) from  base where {queryString};"
		cur.execute(sql,tuple(para))
		rec=cur.fetchone()
		recCount=rec[0]
	else:
		recCount=0
	sql=f"select xid,ch_name, concat(area,addr), group_no, concat(home_tel,',',office_tel,',',bbcall), identif_no from base where {queryString} order by xid desc limit {limitN},30;"
	#print(sql)
	#print(para)
	cur.execute(sql,tuple(para))
	#cur.execute(sql)
	records = cur.fetchall()
	result=[]
	for (xid,name, area, group_no , tel, ID) in records:
		temp={
			"xid": xid,
			"name": name,
			"addr": area,
			"grp": group_no,
			"tel": tel,
			"id": ID
		}
		#print(temp)
		result.append(temp)
	
		#if isinstance(o, datetime):
		#	o=o.strftime('%Y-%m-%d %H:%M:%S')
		#elif isinstance(o, date):
		#	o=o.strftime('%Y-%m-%d')
	print(json.dumps([recCount,result],ensure_ascii=True))
	
def deleteRecord():
	try:
		xid=int(form.getvalue('i'))
	except:
		exit()

	sql=f"select count(*) as c from fundx where bID = {xid}";
	cur.execute(sql)
	r=cur.fetchone()

	if r:
		if r[0] == 0:
			sql=f"delete from base where xid={xid}"
			cur.execute(sql)
			sql=f"delete from validyy where bid={xid}"
			cur.execute(sql)
			#sql=f"delete from baselog where xid={xid}"
			#cur.execute(sql)

			conn.commit()
			msg={"msg":""}
		else:
			msg={"msg":"已有捐款資料，不可刪除!"}
	else:
		msg={"msg":"伺服器錯誤!"}
	print(json.dumps(msg,ensure_ascii=True))


#main starts here
form = cgi.FieldStorage()

try:
	act=form.getvalue('o')
except:
	#print("o missing")
	exit()

#we can start accessing DB now
if act=='g': #get one record by xid
	getRecord()
elif act=='s': #set DB with posted data by xid
	setRecord()
elif act=='f': #find
	findRecords()
elif act=='d': #delete
	deleteRecord()
