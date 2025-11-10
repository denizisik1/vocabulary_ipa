"""Tests for database connection and basic query execution using sqlite3."""

import sqlite3
import os


def test_db_exists():
    assert os.path.exists("pronunciations.db"), "Database file does not exist."


def test_basic_query_operations():
    conn = sqlite3.connect("pronunciations.db")
    cur = conn.cursor()

    cur.execute("SELECT 1;")
    assert cur.fetchone()[0] == 1

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    first_table = cur.fetchone()
    assert first_table, "No tables found in database."

    table_name = first_table[0]
    cur.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cur.fetchone()[0]
    assert count >= 0, f"Invalid count from {table_name}"

    conn.close()


def test_tables_exist():
    conn = sqlite3.connect("pronunciations.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0] for row in cur.fetchall()}
    conn.close()

    expected = {"german"}
    missing = expected - tables
    assert not missing, f"Missing tables: {missing}"
