from config.db_config import DatabaseConfig
from database.json_db import JsonDatabase
from entity.chat_entity import ChatEntity
import time


class ChatLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
        self.db_handel: dict = self.db_client.db_content

    def send_message(self, chat_entity: ChatEntity) -> None:
        chat_entity.timestamp = time.time()
        chat_dict: dict = dict(chat_entity.__dict__)
        self.db_handel["message"].append(chat_dict)
        self.db_client.save_data(content=self.db_handel)

    def select_message_list(self) -> list:
        message_list: list = self.db_handel.get("message", [])
        if not message_list:
            return self.db_handel.get("message", [])
        message_list.sort(key=lambda message: message.get("timestamp"))
        return message_list

    def select_message_count(self) -> int:
        return len(self.select_message_list())
