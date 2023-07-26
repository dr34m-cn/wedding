from utils import utilTools
from service import withMysql


keyInit = withMysql.getStatus()['key']

def getByJscode(req):
    openId = utilTools.getOpenId(req['code'])
    cjKey = req['cjKey']
    return getByOpenId({
        "openId": openId,
        "cjKey": cjKey
    })


def getByOpenId(req):
    openId = req['openId']
    cjKey = req['cjKey']
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
        