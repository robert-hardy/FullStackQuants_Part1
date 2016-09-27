import sqlite3 as sqlite

def connect_db(filename="app/db.sqlite"):
    conn = sqlite.connect(filename)
    init_tables(conn)
    conn.row_factory = dict_factory
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


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
