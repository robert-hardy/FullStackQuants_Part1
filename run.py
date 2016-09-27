from http.server import HTTPServer, BaseHTTPRequestHandler
from random import randint


html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p id="change-me">Here are some buttons:</p>
        {0}
    </body>
</html>"""


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_button = "<div><button>Press me!</button></div>" * randint(0,10)
        html_content = html_template.format(html_button)

        self.wfile.write(bytes(html_content, 'utf-8'))


httpd = HTTPServer(("", 8080), handler)
print("Serving on port 8080")
httpd.serve_forever()
