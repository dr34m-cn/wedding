import requests
import json

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
    if rst['errcode'] == 0:
        return rst['openid']
    elif rst['errcode'] == 40226:
        raise Exception("请更换微信后再试")
    else:
        raise Exception("系统繁忙，请稍后再试")

if __name__ == '__main__':
    print(getOpenId('xxx'))