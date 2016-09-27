from http.server import HTTPServer, BaseHTTPRequestHandler


html_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p id="change-me">Here is some content</p>
    <script>
        var foo = document.getElementById("change-me");
        foo.textContent = "Changed by JavaScript!";
    </script>
    </body>
</html>"""


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(html_content, 'utf-8'))


httpd = HTTPServer(("", 8080), handler)
print("Serving on port 8080")
httpd.serve_forever()
