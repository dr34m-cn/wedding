from common import commonService


# 获取key及状态
def getStatus():
    conn = commonService.connect_mysql()
    cursor = conn.cursor()
    cursor.execute("select `status`,`key` from `conf` where id = %s", (1))
    rst = cursor.fetchone()
    cursor.close()
    conn.close()
    return {
        "status": rst[0],
        "key": rst[1]
    }

# 获取当前用户信息
def getByOpenId(openId):
    conn = commonService.connect_mysql()
    cursor = conn.cursor()
    cursor.execute("select `openId`,id,`status`,`reword` from `userList` where openId = %s", (openId))
    rst = cursor.fetchone()
    cursor.close()
    conn.close()
    if rst is None:
        return None
    else:
        return {
            "openId": rst[0],
            "num": rst[1],
            "status": rst[2],
            "reword": rst[3]
        }

# 新建用户
def newUser(openId):
    conn = commonService.connect_mysql()
    cursor = conn.cursor()
    cursor.execute("insert into userList(`openId`) values(%s)", (openId))
    lastId = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return lastId

# 更新中奖状态
def updateStatus(openId, reword):
    conn = commonService.connect_mysql()
    cursor = conn.cursor()
    cursor.execute("update userlist set `status` = 1, `reword` = %s where openId = %s", (reword, openId))
    conn.commit()
    cursor.close()
    conn.close()