import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Return a new database connection.

    Environment variables (loaded from .env) determine how to connect. For
    local development the default uses a Postgres server running on
    ``localhost:5432`` with the credentials below. If the connection fails a
    helpful message is logged so you can verify that Postgres is running and
    the parameters are correct.
    """
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
    except psycopg2.OperationalError as exc:
        # Provide a more user-friendly hint than the raw psycopg2 traceback
        raise RuntimeError(
            "Unable to connect to the Postgres database. "
            "Make sure a Postgres server is running on the host specified by "
            "DB_HOST (typically localhost) and that the credentials in .env "
            "are correct.\nOriginal error: %s" % exc
        ) from exc

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
