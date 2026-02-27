import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    # Drop existing table if it exists
    cur.execute("DROP TABLE IF EXISTS todos CASCADE")

    # Create fresh table with timestamp
    cur.execute("""
    CREATE TABLE todos(
        id SERIAL PRIMARY KEY,
        task TEXT NOT NULL,
        status BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
