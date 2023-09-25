import os
import json
from io import TextIOWrapper
from config.db_config import DatabaseConfig


class JsonDatabase:
    def __init__(self, db_path: str = DatabaseConfig.json_db_path) -> None:
        if not os.path.exists(db_path):
            os.makedirs(db_path)
        self.db_handel: TextIOWrapper = open(db_path, mode="r+", encoding="u8")        
        self.db_content: dict = json.loads(self.db_handel.read())
    
    def init_db(self) -> None:
        self.db_handel.write(json.dumps(DatabaseConfig.origin_db_conent))
    
    def select_user_info_list(self) -> list:
        return self.db_content.get("user_list", [])

    def select_user_info_by_id(self, id: int) -> dict:
        user_list: list = self.select_user_info_list()
        if result := [item for item in user_list if item["id"] == id]:                    
            return result[0]
        return {}
    
    def select_user_count(self) -> int:
        return self.db_content.get("user_count", 0)

    def select_message_list(self) -> list:
        return self.db_content.get("message_list", [])       
    
    def __del__(self) -> None:
        self.db_handel.close()

