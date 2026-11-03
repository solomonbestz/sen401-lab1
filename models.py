"""
Module: models.py
Description: SQLite Database persistence layer for Lab 4 migration.
Author: Solomon Azowenu
"""
import sqlite3
from typing import List, Dict, Any

DB_NAME = "database.db"

def init_db():
    """Initializes SQLite database and seeds initial records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score REAL NOT NULL
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO students (name, score) VALUES (?, ?)",
            [("Solomon Azowenu", 95.0), ("James", 45.0), ("Deborah", 82.0)]
        )
        conn.commit()
    conn.close()

def get_all_students() -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, score FROM students")
    rows = cursor.fetchall()
    result = [dict(row) for row in rows]
    conn.close()
    return result

def add_student_db(name: str, score: float) -> int:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id