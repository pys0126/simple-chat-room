import os
from config.project_config import ProjectConfig

# 定义启动命令
command: str = f"gunicorn init:app -b {ProjectConfig.host}:{ProjectConfig.port} -w {ProjectConfig.workers}"

if __name__ == "__main__":
    os.system(command=command)