from lib import socketserver
from lib.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json
import cgi

def getParams(uri):
    if "?" in uri:
        param=uri.split("?")
        param=param[1]
        param=parse_qs(param)
        return param
    return {}

class MyHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

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
        params=getParams(self.path)

        if self.path.startswith('/multiplication'):
            try:
                a=params["a"][0]
            except:
                self.sendContent("fail", "Parameter a is missing")
                return

            try:
                b=params["b"][0]
            except:
                self.sendContent("fail", "Parameter b is missing")
                return

            try:
                a=float(a)
                b=float(b)
                result=a*b
                self.sendContent("success", {"result": result})
                return
            except:
                self.sendContent("error", "Error during computation")
                return


print("Listening...")
httpd = socketserver.TCPServer(("", 80), MyHandler)
httpd.serve_forever()
