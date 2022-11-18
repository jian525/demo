# 連線DB
from dbConfig import conn, cur


def getList():
    # 查詢
    sql = "select id, title,msg, nickname,likes from guestbook order by likes desc;"
    cur.execute(sql)

    records = cur.fetchall()
    # return records
    ret = []

    for (id, title, msg, nick, likes) in records:
        temp = {
            'id': id,
            'title': title,
            'likes': likes
        }
        # print(temp)
        ret.append(temp)

    return ret


# def like(id):
    #global cur, conn
    #sql = "update guestbook set likes=likes+1 where id=%s;"
    #sql = "delete from guestbook where id=%s;"
    #cur.execute(sql, (id,))
    # conn.commit()
def add(id):
    global cur, conn
    sql = "add to guestbook where id=%s;"
    #sql = "delete from guestbook where id=%s;"
    cur.execute(sql, (id,))
    conn.commit()


def kill(id):
    global cur, conn
    sql = "delete from guestbook where id=%s;"
    cur.execute(sql, (id,))
    conn.commit()
