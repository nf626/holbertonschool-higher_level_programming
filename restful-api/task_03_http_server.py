"""http server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


PORT = 8000

class HTTP_Class(BaseHTTPRequestHandler):
    """subclass"""
    def do_GET(self):
        """do_GET method"""
        if self.path == '/':
        # status code to client
            self.send_response(200)
            self.end_headers()
        # write the HTTP response headers and body
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
        # json data
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(data.encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_error(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# If this script is the main entry point, start the server on port 8000
if __name__ == "__main__":
    httpd = HTTPServer(('', PORT), HTTP_Class)
    httpd.serve_forever(PORT)
