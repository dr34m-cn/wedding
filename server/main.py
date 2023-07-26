import json

import urllib3
from common.commonService import get_logger as GL, get_post_data as GD, ResultMap as RS
from service import weddingService
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class getByJscode(RequestHandler):
    def post(self):
        try:
            req = GD(self)
            msg = RS(weddingService.getByJscode(req))
        except Exception as e:
            msg = RS(str(e), 500)
        self.write(msg)

if __name__ == "__main__":

    urllib3.disable_warnings()

    GL(1)

    with open('conf.json','r') as fileConf:
        conf = json.loads(fileConf.read())
    
    # 启动端口
    port = conf['server']['port']

    app = Application([
        (r"/getByJscode", getByJscode)
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
