from entity.user_entity import UserEntity
from entity.chat_entity import ChatEntity
import json


def dict_to_user(dict_obj: dict) -> UserEntity:
    return UserEntity(user_id=dict_obj.get("user_id"),
                      username=dict_obj.get("username"),
                      password=dict_obj.get("password"),
                      nikename=dict_obj.get("nikename"))


def dict_to_chat(dict_obj: dict) -> ChatEntity:
    return ChatEntity(user_id=dict_obj.get("user_id"),
                      content=dict_obj.get("content"))


chat_decoder: json.JSONDecoder = json.JSONDecoder(object_hook=dict_to_chat)
user_decoder: json.JSONDecoder = json.JSONDecoder(object_hook=dict_to_user)

