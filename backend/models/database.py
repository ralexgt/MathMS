import sqlite3
from pathlib import Path

# root/backend/database.db
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.db"


# Create a new connection and a new cursor for every request
# to avoid issues with concurrent access issues
class Database:
    def __init__(self, db_path: Path = DB_PATH):
        self.connection = (
            sqlite3.connect(db_path.as_posix(), check_same_thread=False))
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
