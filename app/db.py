import sqlite3 as sqlite

def connect_db(filename="app/db.sqlite"):
    conn = sqlite.connect(filename)
    init_tables(conn)
    return conn


def init_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS
            todo
        (
            id INTEGER PRIMARY KEY,
            title TEXT,
            notes TEXT
        )
    """)
    conn.commit()
