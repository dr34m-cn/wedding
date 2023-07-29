from utils import utilTools
from service import withMysql


status = withMysql.getStatus()
keyInit = status['key']
frontKey = status['frontKey']

def getByJscode(req):
    openId = utilTools.getOpenId(req['code'])
    cjKey = req['cjKey'] if 'cjKey' in req else None
    return getByOpenId({
        "openId": openId,
        "cjKey": cjKey
    })


def getByOpenId(req):
    openId = req['openId']
    cjKey = req['cjKey'] if 'cjKey' in req else None
    user = withMysql.getByOpenId(openId)
    if user is None:
        if cjKey is None:
            raise Exception("未找到信息")
        elif cjKey == keyInit:
            idNum = withMysql.newUser(openId)
            user = {
                "openId": openId,
                "num": idNum,
                "status": 0,
                "reword": 0
            }
        else:
            raise Exception("抽奖码有误")
    user['num'] = utilTools.getNumById(user['num'])
    return user

def getAllUser(req):
    checkFrKey(req)
    return withMysql.getAll()


def setUserStatus(req):
    checkFrKey(req)
    userId = req['userId']
    reword = req['reword']
    withMysql.updateStatus(userId, reword)
    return None


def checkFrKey(req):
    frKey = req['frKey']
    if frKey != frontKey:
        raise Exception("秘钥有误")