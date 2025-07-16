import sqlite3
from pathlib import Path
from datetime import datetime

# root/backend/database.db
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.db"

class Database:
    def __init__(self, db_path: Path = DB_PATH):
        self.connection = sqlite3.connect(db_path.as_posix(), check_same_thread=False)
        self.cursor = self.connection.cursor()
        self._initialize_db()

    def _initialize_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endpoint TEXT,
                operation TEXT,
                arguments TEXT,
                result TEXT,
                status_code INTEGER,
                timestamp TEXT
            )
        """)
        self.connection.commit()

    def log_request(self, endpoint: str, operation: str, arguments: str,
                    result: str, status_code: int):
        self.cursor.execute(
            """INSERT INTO logs
            (endpoint, operation, arguments, result, status_code, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (endpoint, operation, arguments, result, status_code,
             datetime.now().isoformat())
        )
        self.connection.commit()
    
    def read_logs(self, limit=100):
        logs = self.cursor.execute(
             """SELECT
                   id, endpoint, operation, arguments, 
                   result, status_code, timestamp 
                FROM logs
                ORDER BY id DESC LIMIT ?""",
            (limit,)
        ).fetchall()

        for log in logs:
            print(log) # TODO: will change