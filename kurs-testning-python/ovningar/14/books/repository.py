# repository.py
import sqlite3


class BookRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        conn = self._get_conn()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self._get_conn()
        rows = conn.execute("SELECT * FROM books").fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_by_id(self, book_id):
        conn = self._get_conn()
        row = conn.execute(
            "SELECT * FROM books WHERE id = ?", (book_id,)
        ).fetchone()
        conn.close()
        return dict(row) if row else None

    def create(self, title, author):
        conn = self._get_conn()
        cursor = conn.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author),
        )
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return self.get_by_id(book_id)

    def update(self, book_id, title=None, author=None):
        book = self.get_by_id(book_id)
        if not book:
            return None
        conn = self._get_conn()
        new_title = title if title else book["title"]
        new_author = author if author else book["author"]
        conn.execute(
            "UPDATE books SET title = ?, author = ? WHERE id = ?",
            (new_title, new_author, book_id),
        )
        conn.commit()
        conn.close()
        return self.get_by_id(book_id)

    def delete(self, book_id):
        book = self.get_by_id(book_id)
        if not book:
            return False
        conn = self._get_conn()
        conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        return True
