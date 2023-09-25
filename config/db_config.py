from config.project_config import ProjectConfig
import os


class DatabaseConfig:
    json_db_path: str = os.path.join(ProjectConfig.base_dir, "database/database.json")
    origin_db_conent: dict = {
    "user_list": [
        {
            "id": 1,
            "username": "admin",
            "nikename": "主人",
            "password": "xxx"
        },
        {
            "id": "2",
            "username": "root",
            "nikename": "小猫咪",
            "password": "xxx"
        }
    ],
    "user_count": 2,
    "message_list": [
        {
            "user_id": 1,
            "content": "test"
        }
    ]
}