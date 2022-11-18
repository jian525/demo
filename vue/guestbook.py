#連線DB
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select id, title,msg, nickname,likes from guestbook order by likes desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delMsg(id):
    sql="delete from guestbook where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def likeMsg(id,vipNumber=0):
    if vipNumber>0:
        sql="update guestbook set likes=likes+100 where id=%s;"
        
    else:
        sql="update guestbook set likes=likes+1 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def addMsg(title,msg, nick):
    sql="insert into guestbook (title,msg,nickname) values (%s,%s,%s);"
    cur.execute(sql,(title,msg,nick))
    conn.commit()
    return False

