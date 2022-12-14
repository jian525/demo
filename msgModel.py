# 連線DB
from dbConfig import conn, cur


def getList():
    # 查詢
    sql = "select id, title,msg,likes, nickname from guestbook order by id desc;"
    cur.execute(sql)

    records = cur.fetchall()
    # return records
    ret = []

    for (id, title, msg, likes, nick) in records:
        temp = {
            'id': id,
            'title': title,
            'msg': msg,
            'nick': nick,  # 價錢
            'likes': likes
        }
        # print(temp)
        ret.append(temp)

    return ret


def getcartList():
    # 查詢
    sql = "select id,likes, nickname from guestbook order by likes desc;"
    cur.execute(sql)

    list = cur.fetchall()
    # return records
    res = []

    for (id, likes, nick) in list:
        temp = {
            'id': id,
            'nick': nick,  # 價錢
            'likes': likes
        }
        # print(temp)
        res.append(temp)
    return res


def like(id):
    global cur, conn
    sql = "update guestbook set likes=likes+1 where id=%s;"
    cur.execute(sql, (id,))
    conn.commit()


def kill(id):
    global cur, conn
    sql = "delete from guestbook where id=%s;"
    cur.execute(sql, (id,))
    conn.commit()
