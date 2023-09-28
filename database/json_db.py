import os
import json
from config.db_config import DatabaseConfig


class JsonDatabase:
    def __init__(self, db_path: str = DatabaseConfig.json_db_path) -> None:
        self.db_path: str = db_path
        if not os.path.exists(path=self.db_path):
            os.makedirs(name=self.db_path)
        self.db_content: dict = self.read_db_content()
    
    def init_db(self) -> None:
        with open(file=self.db_path, mode="w", encoding="u8") as f:
            f.write(json.dumps(DatabaseConfig.origin_db_content, ensure_ascii=False, indent=4))

    def read_db_content(self) -> dict:
        with open(file=self.db_path, mode="r", encoding="u8") as f:
            content: str = f.read()
        return json.loads(content)

    def save_data(self, content: dict) -> None:
        with open(file=self.db_path, mode="w", encoding="u8") as f:
            f.write(json.dumps(content, ensure_ascii=False, indent=4))