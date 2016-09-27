from flask import (
    Flask,
    Response
)


from random import randint


the_app = Flask(__name__)


html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p id="change-me">Here are some buttons:</p>
        {0}
        <p>Here are some more buttons:</p>
        <div id="some-more-buttons"></div>
    <script>
        var foo = document.getElementById("some-more-buttons");
        var html_buttons = "<div><button>Client side.</button></div>".repeat(Math.random() * 10);
        foo.innerHTML = html_buttons;
    </script>
    </body>
</html>"""

html_button = "<div><button>Server side.</button></div>" * randint(0,10)
html_content = html_template.format(html_button)


@the_app.route('/')
def homepage():
    return Response(html_content)


@the_app.route('/page1')
def page1():
    return Response(html_content)


the_app.run('0.0.0.0', port=8080)
