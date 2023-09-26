from config.db_config import DatabaseConfig
from database.json_db import JsonDatabase


class ChatLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
        self.db_handel: dict = self.db_client.db_content

    def select_message_list(self) -> list:
        return self.db_handel.get("message", [])

    def select_message_count(self) -> int:
        return len(self.select_message_list())
