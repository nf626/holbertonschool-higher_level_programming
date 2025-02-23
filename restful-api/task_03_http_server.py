"""http server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


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
        # Page language
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
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def start_server(address='', port=8000, server_class=HTTPServer, Handler_class=HTTP_Class):
    """Server initialised and start"""
    server_address = (address, port)
    http_server = server_class(server_address, Handler_class)
    print(f"Starting server on: LocalHost - {port}")
    http_server.serve_forever()
    

# If this script is the main entry point, start the server on port 8000
if __name__ == "__main__":
    start_server()
