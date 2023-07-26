from utils.code2openid import getOpenId

def getByJscode(req):
    openId = getOpenId(req['code'])
    return openId