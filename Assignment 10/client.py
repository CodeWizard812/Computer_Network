import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

port = 8888
server_address = ("", port)
httpd = HTTPServer(server_address, CustomHandler)

print(f"Server port: {port}")

# Continuously open pages
while True:
    # Ask the user for input
    page = input("Enter the page you want to open (or type 'quit' to exit): ")

    if page.lower() == 'quit':
        break

    # Open the browser to the specified page
    webbrowser.open(f"http://localhost:{port}/{page}")

httpd.server_close()
