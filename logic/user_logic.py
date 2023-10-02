import json

from flask import session

from entity.user_entity_vo import UserEntityVO
from util.string_util import create_uuid
from database.json_db import JsonDatabase
from entity.user_entity import UserEntity
from config.status_code import StatusCode
from util.json_util import user_vo_decoder
from config.db_config import DatabaseConfig
from exception.custom_exception import CustomException


class UserLogic:
    def __init__(self) -> None:
        self.db_client: JsonDatabase = JsonDatabase(db_path=DatabaseConfig.json_db_path)
        self.db_handel: dict = self.db_client.db_content

    def login(self, user_entity: UserEntity) -> dict:
        # 根据username查询用户信息
        user_info: dict = self.select_user_info_by_username(username=user_entity.username)
        print(dict(user_entity.__dict__))
        print(user_info)
        # 判断用户名和密码是否正确
        if not user_info or user_info.get("password") != user_entity.password:
            raise CustomException(error_code=StatusCode.LOGIN_ERROR.value, message="用户名或密码错误")
        # 获取用户ID
        user_id: int = user_info.get("user_id")
        user_info_vo: UserEntityVO = user_vo_decoder.decode(json.dumps(user_info))
        user_info_vo_dict: dict = dict(user_info_vo.__dict__)
        # 根据用户ID将用户信息存入session，返回用户信息
        session["user"] = user_id
        return user_info_vo_dict

    def register(self, user_entity: UserEntity) -> None:
        # 判断用户名、密码、昵称是否为空字符
        if not all([user_entity.username, user_entity.password, user_entity.nikename]):
            raise CustomException(error_code=StatusCode.REGISTER_ERROR.value, message="请完善信息")
        # 根据username判断用户是否存在
        if self.select_user_info_by_username(username=user_entity.username):
            raise CustomException(error_code=StatusCode.REGISTER_ERROR.value, message="用户名已存在")
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
        session.pop("user")

    def select_user_count(self) -> int:
        return len(self.select_user_info_list())

    def select_user_info_by_id(self, user_id: str) -> dict:
        user_list: list = self.select_user_info_list()
        if result := [item for item in user_list if item["user_id"] == user_id]:
            user_info_vo: UserEntityVO = user_vo_decoder.decode(json.dumps(result[0]))
            user_info_vo_dict: dict = dict(user_info_vo.__dict__)
            return user_info_vo_dict
        return {}

    def select_user_info_by_username(self, username: str) -> dict:
        user_list: list = self.select_user_info_list()
        if result := [item for item in user_list if item.get("username") == username]:
            return result[0]
        return {}

    def select_user_info_list(self) -> list:
        user_info_list: list = self.db_handel.get("user", [])
        new_user_info_list: list = []
        for user_info in user_info_list:
            new_user_info_list.append(user_info)
        return new_user_info_list

    def select_now_user_info(self) -> dict:
        user_id: str = session.get("user")
        user_info: dict = self.select_user_info_by_id(user_id=user_id)
        if not user_info:
            raise CustomException(error_code=StatusCode.ACCESS_DENIED.value, message="拒绝访问")
        return user_info

