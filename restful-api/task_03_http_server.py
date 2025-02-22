"""http server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler


PORT = 8000

class HTTP_Class(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

httpd = HTTPServer(('', PORT), HTTP_Class)
httpd.serve_forever()
