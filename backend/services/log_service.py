from datetime import datetime

from models.database import Database
from models.log_model import Log
from utils.logger import logger


class LogService():
    def __init__(self, db: Database):
        self.db = db

    def log_request(self, endpoint: str, operation: str, arguments: str,
                    result: str, status_code: int):
        self.db.cursor.execute(
            """INSERT INTO logs
            (endpoint, operation, arguments, result, status_code, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (endpoint, operation, arguments, result, status_code,
             datetime.now().isoformat())
        )
        self.db.connection.commit()
        logger.info(
            f"Logged request: {endpoint} {operation} {arguments} -> {result} "
            f"Status: {status_code}"
        )

    def read_logs(self, limit=100):
        logs = self.db.cursor.execute(
            """SELECT
                   id, endpoint, operation, arguments,
                   result, status_code, timestamp
                FROM logs
                ORDER BY id DESC LIMIT ?""",
            (limit,)
        ).fetchall()
        logger.info(f"Retrieved {len(logs)} logs from the database.")

        return [Log(
            id=log[0],
            endpoint=log[1],
            operation=log[2],
            arguments=log[3],
            result=log[4],
            status_code=log[5],
            timestamp=log[6]
        ) for log in logs]
