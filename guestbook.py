from dbConfig import conn, cur
def getList():
    sql="select id,title,msg,nickname,likes from guestbook"
    cur.execute(sql)
    records=cur.fetchall()
    return records
def delMsg(id):
    sql="delete from guestbook where id=%s;"
    cur.execute(sql,(id,))#,不可省略  可傳多個參數
    conn.commit()
    return True
def addMsg(title,msg,nickname):
    sql="insert into guestbook (title,msg,nickname) values (%s,%s,%s);"
    cur.execute(sql,(title,msg,nickname))
    conn.commit()
    return False
def likeMsg(id):
    sql="update guestbook set likes=likes+1 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
def getDetail(id):
    return None