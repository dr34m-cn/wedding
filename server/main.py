import json

import urllib3
from common import commonService
from service import ocrService
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class ocr(RequestHandler):
    def post(self):
        try:
            req = commonService.get_post_data(self)
            msg = commonService.ResultMap(ocrService.doOCR(req))
        except Exception as e:
            msg = commonService.ResultMap(str(e), 500)
        self.write(msg)

if __name__ == "__main__":

    urllib3.disable_warnings()

    commonService.get_logger(1)

    with open('conf.json','r') as fileConf:
        conf = json.loads(fileConf.read())
    
    # 启动端口
    port = conf['server']['port']

    app = Application([
        (r"/ocr", ocr)
    ])

    # 单线程启动
    # app.listen(port)
    
    # IOLoop.current().start()


    # 多线程启动（必须Linux系统下启动）
    # 线程数
    thread = conf['server']['thread']
    http_server = httpserver.HTTPServer(app)
    http_server.bind(port)
    http_server.start(thread)

    IOLoop.instance().start()
