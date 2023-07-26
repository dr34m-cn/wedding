import json

import requests

with open('conf.json','r') as fileConf:
    conf = json.loads(fileConf.read())

def getOpenId(code):
    mp = conf['wechat']
    url = "https://api.weixin.qq.com/sns/jscode2session"
    params = {
        "appid": mp['appId'],
        "secret": mp['AppSecret'],
        "js_code": code,
        "grant_type": 'authorization_code'
    }
    rst = json.loads(requests.get(url, params).text)
    if 'errcode' not in rst:
        return rst['openid']
    elif rst['errcode'] == 40226:
        raise Exception("请更换微信后再试")
    else:
        raise Exception("系统繁忙，请稍后再试")

def getNumById(idNum):
    num = 'A'
    if idNum < 10:
        num = 'A00'+str(idNum)
    elif idNum < 100:
        num = 'A0'+str(idNum)
    else:
        num = 'A'+str(idNum)
    return num