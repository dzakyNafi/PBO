import sqlite3
import pandas as pd
from konfigurasi import DB_PATH


def get_db_connection():
    try:
        conn = sqlite3.connect(
            DB_PATH,
            timeout=10,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"ERROR koneksi database: {e}")
        return None


def execute_query(query, params=None):
    conn = get_db_connection()

    if not conn:
        return None

    try:
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()

        if query.strip().upper().startswith("INSERT"):
            return cursor.lastrowid

        return cursor.rowcount

    except sqlite3.Error as e:
        print(f"ERROR execute query: {e}")
        conn.rollback()
        return None

    finally:
        conn.close()


def fetch_query(query, params=None, fetch_all=True):
    conn = get_db_connection()

    if not conn:
        return None

    try:
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch_all:
            return cursor.fetchall()

        return cursor.fetchone()

    except sqlite3.Error as e:
        print(f"ERROR fetch query: {e}")
        return None

    finally:
        conn.close()


def get_dataframe(query, params=None):
    conn = get_db_connection()

    if not conn:
        return pd.DataFrame()

    try:
        return pd.read_sql_query(query, conn, params=params)

    except Exception as e:
        print(f"ERROR dataframe: {e}")
        return pd.DataFrame()

    finally:
        conn.close()


def setup_database_initial():
    conn = get_db_connection()

    if not conn:
        return False

    try:
        cursor = conn.cursor()

        sql_create_table = """
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            deskripsi TEXT NOT NULL,
            jumlah REAL NOT NULL CHECK(jumlah > 0),
            kategori TEXT,
            tanggal DATE NOT NULL
        );
        """

        cursor.execute(sql_create_table)
        conn.commit()

        print("Tabel transaksi siap")
        return True

    except sqlite3.Error as e:
        print(f"ERROR setup database: {e}")
        return False

    finally:
        conn.close()