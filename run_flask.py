from flask import (
    render_template
)


from app.db import connect_db
from app.flasky import the_app


@the_app.route('/')
def homepage():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("select * from todo;")
    rows = cur.fetchall()
    return render_template(
        'homepage.html',
        rows = rows
    )


the_app.run('0.0.0.0', port=8080)
