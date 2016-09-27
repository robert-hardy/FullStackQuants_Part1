from flask import (
    render_template
)


from app.flasky import the_app


@the_app.route('/')
def homepage():
    return render_template(
        'homepage.html'
    )


the_app.run('0.0.0.0', port=8080)
