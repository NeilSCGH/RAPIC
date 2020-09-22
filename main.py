from lib import socketserver
from lib.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json
import cgi
from functions import *

def getParams(uri):
    if "?" in uri:
        param=uri.split("?")
        param=param[1]
        param=parse_qs(param)
        return param
    return {}

class MyHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return #remove red log messages

    def sendContent(self,status, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content = json.dumps({'Status': status, "data": data})
        content =str.encode(content)
        self.wfile.write(content)

    def do_GET(self):
        if self.path == "/favicon.ico":
            return
        if self.path == "/":
            self.sendContent("success", "Hello")

        print("GET {}".format(self.path))
        self.params=getParams(self.path)

        if self.path.startswith('/addition'):
            addition(self)
        elif self.path.startswith('/multiplication'):
            multiplication(self)

print("Listening...")
httpd = socketserver.TCPServer(("", 80), MyHandler)
httpd.serve_forever()
