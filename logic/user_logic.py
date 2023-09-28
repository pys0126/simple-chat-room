from flask import session
from util.string_util import create_uuid
from database.json_db import JsonDatabase
from entity.user_entity import UserEntity
from config.status_code import StatusCode
from util.string_util import calculate_md5
from config.db_config import DatabaseConfig
from exception.custom_exception import CustomException


class UserLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
        self.db_handel: dict = self.db_client.db_content

    def login(self, user_entity: UserEntity) -> dict:
        # 根据username查询用户信息
        user_info: dict = self.select_user_info_by_username(username=user_entity.username)
        # 判断用户名和密码是否正确
        if not user_info or user_info.get("password") != user_entity.password:
            raise CustomException(error_code=StatusCode.LOGIN_ERROR.value, message="用户名不存在或密码错误")
        # 获取用户ID
        user_id: int = user_info.get("user_id")
        # 根据用户ID将用户信息存入session，返回用户信息
        session[user_id] = user_info
        return user_info

    def register(self, user_entity: UserEntity) -> None:
        # 判断用户名、密码、昵称是否为空字符
        if not all([user_entity.username, user_entity.password, user_entity.nikename]):
            raise CustomException(error_code=StatusCode.REGISTER_ERROR.value, message="请完善信息")
        # 根据username判断用户是否存在
        if self.select_user_info_by_username(username=user_entity.username):
            raise CustomException(error_code=StatusCode.REGISTER_ERROR.value, message="用户名已存在")
        # 将密码加密
        user_entity.password = calculate_md5(user_entity.password)
        # 设置用户ID
        user_entity.user_id = create_uuid()
        # 将UserEntity转为dict，更新数据
        user_info: dict = dict(user_entity.__dict__)
        self.db_handel["user"].append(user_info)
        # 存入数据库
        self.db_client.save_data(content=self.db_handel)

    def logout(self, user_id: str) -> None:
        # 判断该user_id的用户是否存在
        if not self.select_user_info_by_id(user_id=user_id):
            raise CustomException(error_code=StatusCode.NOTFOUND.value, message="该用户不存在")
        # 获取所有用户信息列表
        user_info_list: list = self.select_user_info_list()
        # 去除该user后的列表
        new_user_info_list: list = [item for item in user_info_list if item["user_id"] != user_id]
        # 更新数据
        self.db_handel["user"] = new_user_info_list
        # 写入数据库
        self.db_client.save_data(content=self.db_handel)

    def select_user_count(self) -> int:
        return len(self.select_user_info_list())

    def select_user_info_by_id(self, user_id: str) -> dict:
        user_list: list = self.select_user_info_list()
        if result := [item for item in user_list if item["user_id"] == user_id]:
            return result[0]
        return {}

    def select_user_info_by_username(self, username: str) -> dict:
        user_list: list = self.select_user_info_list()
        if result := [item for item in user_list if item["username"] == username]:
            return result[0]
        return {}

    def select_user_info_list(self) -> list:
        user_info_list: list = self.db_handel.get("user", [])
        new_user_info_list: list = []
        for user_info in user_info_list:
            # 删除password字段
            user_info.pop("password")
            new_user_info_list.append(user_info)
        return new_user_info_list
