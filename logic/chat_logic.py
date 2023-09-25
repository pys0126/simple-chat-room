from service.chat_service import ChatService
from config.db_config import DatabaseConfig
from database.json_db import JsonDatabase


class ChatLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
    
    def select_message_list(self) -> list:
        return self.db_client.select_message_list()        

    def select_user_count(self) -> int:
        return self.db_client.select_user_count()

    def select_user_info_by_id(self, id: int) -> dict:
        return self.db_client.select_user_info_by_id(id=id)

    def select_user_info_list(self) -> list:
        return self.db_client.select_user_info_list()    
