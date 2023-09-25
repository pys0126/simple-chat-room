from database.json_db import JsonDatabase
from config.db_config import DatabaseConfig


class UserLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
    
    def login(self, username: str, password: str) -> None:
        ...
    
    def register(self, username: str, nikename: str, password: str) -> None:
        ...