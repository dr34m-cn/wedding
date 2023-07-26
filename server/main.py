import json

import urllib3
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from common import commonService as CS
from service import weddingService


class getByJsCode(RequestHandler):
    def post(self):
        try:
            req = CS.get_post_data(self)
            msg = CS.ResultMap(weddingService.getByJscode(req))
        except Exception as e:
            msg = CS.ResultMap(str(e), 500)
        self.write(msg)

class getByOpenId(RequestHandler):
    def post(self):
        try:
            req = CS.get_post_data(self)
            msg = CS.ResultMap(weddingService.getByOpenId(req))
        except Exception as e:
            msg = CS.ResultMap(str(e), 500)
        self.write(msg)

if __name__ == "__main__":

    urllib3.disable_warnings()

    CS.get_logger(1)

    with open('conf.json','r') as fileConf:
        conf = json.loads(fileConf.read())
    
    # 启动端口
    port = conf['server']['port']

    app = Application([
        (r"/getByJsCode", getByJsCode),
        (r"/getByOpenId", getByOpenId)
    ])

    # 单线程启动
    app.listen(port)
    
    IOLoop.current().start()


    # 多线程启动（必须Linux系统下启动）
    # 线程数
    # thread = conf['server']['thread']
    # http_server = httpserver.HTTPServer(app)
    # http_server.bind(port)
    # http_server.start(thread)

    # IOLoop.instance().start()
