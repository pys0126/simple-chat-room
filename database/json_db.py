import os
import json
from typing import TextIO
from config.db_config import DatabaseConfig


class JsonDatabase:
    def __init__(self, db_path: str = DatabaseConfig.json_db_path) -> None:
        if not os.path.exists(db_path):
            os.makedirs(db_path)
        self.db_handel: TextIO = open(db_path, mode="w+", encoding="u8")
        self.db_content: dict = json.loads(self.db_handel.read())
    
    def init_db(self) -> None:
        self.db_handel.write(json.dumps(DatabaseConfig.origin_db_content, ensure_ascii=False, indent=4))

    def save_data(self, content: dict) -> None:
        self.db_handel.write(json.dumps(content, ensure_ascii=False, indent=4))

    def __del__(self) -> None:
        self.db_handel.close()

