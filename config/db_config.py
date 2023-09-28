from config.project_config import ProjectConfig
import os


class DatabaseConfig:
    json_db_path: str = os.path.join(ProjectConfig.base_dir, "database/database.json")
    origin_db_content: dict = {
        "user": [
            {
                "user_id": "8187d8b0-331b-4b33-95e5-3e7007b35af5",
                "nikename": "管理员",
                "username": "admin",
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        ],
        "message": []
    }
