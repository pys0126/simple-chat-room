import os
from uuid import uuid4


class ProjectConfig:
    base_dir: str = os.getcwd()
    secret_key: str = str(uuid4())
    host: str = "0.0.0.0"
    port: int = 9898
    workers: int = 1
