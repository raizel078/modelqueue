import sqlite3


def create_connection():
    return sqlite3.connect("database.db")


def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id TEXT PRIMARY KEY,
            mori_name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_job(job_id, mori_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jobs (job_id, mori_name) VALUES (?, ?)",
        (job_id, mori_name)
    )

    conn.commit()
    conn.close()