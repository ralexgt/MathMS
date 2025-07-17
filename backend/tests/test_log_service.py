from unittest.mock import MagicMock

from services.log_service import LogService


class TestLogService:
    def test_log_request_and_read_logs(self):
        mock_db = MagicMock()
        mock_db.cursor.execute.return_value.fetchall.return_value = [
            (1, "/test", "test", "1,2", "3", 200, "2025-07-17T12:00:00")
        ]
        mock_db.connection.commit.return_value = None

        log_service = LogService(mock_db)
        log_service.log_request(
            endpoint="/test",
            operation="test",
            arguments="1,2",
            result="3",
            status_code=200
        )
        logs = log_service.read_logs(limit=1)
        assert len(logs) == 1
        assert logs[0].endpoint == "/test"
        assert logs[0].operation == "test"
        assert logs[0].arguments == "1,2"
        assert logs[0].result == "3"
        assert logs[0].status_code == 200
