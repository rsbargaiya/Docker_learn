from db import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS todos(
        id SERIAL PRIMARY KEY,
        task TEXT,
        status BOOLEAN DEFAULT FALSE,
        user_id INTEGER REFERENCES users(id)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()