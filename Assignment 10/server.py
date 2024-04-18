from http.server import HTTPServer, SimpleHTTPRequestHandler
import base64

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        elif self.path == "/about.html":
            auth_header = self.headers.get('Authorization')
            if auth_header is None or 'Basic ' not in auth_header:
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm="Secure Area"')
                self.end_headers()
                return
            else:
                auth_decoded = base64.b64decode(auth_header.split(' ')[1]).decode('utf-8')
                username, password = auth_decoded.split(':')
                if username =='admin' and password == '12345':
                    self.path = "/about.html"
                else:
                    self.send_response(401)
                    self.send_header('WWW-Authenticate', 'Basic realm="Secure Area"')
                    self.end_headers()
                    return

        return super().do_GET()

port = 8888
server_address = ("", port)
httpd = HTTPServer(server_address, CustomHandler)

print(f"Server is running on port {port}")

httpd.serve_forever()
