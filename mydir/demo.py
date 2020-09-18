"""
Web Server
"""

from socket import *


class WebServer:
    def __init__(self, host='0.0.0.0', port=80, html=0):
        self.host = host
        self.port = port
        self.html = html
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock = socket
        self.sock.setblocking(False)

    def bind(self):
        self.adress = (self.host, self.port)
        self.sock.bind(self.adress)

    def start(self):
        pass


if __name__ == '__main__':
    # 1.使用者怎么利用这个类
    # 2.实现类的功能需要使用者提供什么(传参)
    #      地址     网页
    httpd = WebServer(host='0.0.0.0', port=8000, html='./static')
    httpd.start()
