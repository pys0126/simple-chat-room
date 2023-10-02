from typing import Union
from logic.user_logic import UserLogic
from util.json_util import user_decoder
from config.status_code import StatusCode
from entity.user_entity import UserEntity
from service.user_service import UserService
from flask import Blueprint, jsonify, Response, request, render_template

user_blueprint: Blueprint = Blueprint("user", __name__)
user_logic_object: UserLogic = UserService.init_user_logic()


@user_blueprint.route(rule="/login", methods=["POST"])
def login() -> Response:
    user_entity: UserEntity = user_decoder.decode(s=request.data.decode("u8"))
    user_info: dict = UserService.login(user_logic_object=user_logic_object, user_entity=user_entity)
    return jsonify(code=StatusCode.SUCCESS.value, data=user_info)


@user_blueprint.route(rule="/register", methods=["POST"])
def register() -> Response:
    user_entity: UserEntity = user_decoder.decode(s=request.data.decode("u8"))
    UserService.register(user_logic_object=user_logic_object, user_entity=user_entity)
    return jsonify(code=StatusCode.SUCCESS.value, message="注册成功")


@user_blueprint.route(rule="/logout/<string:user_id>", methods=["POST"])
def logout(user_id: str) -> Response:
    UserService.logout(user_logic_object=user_logic_object, user_id=user_id)
    return jsonify(code=StatusCode.SUCCESS.value, message="注销成功")


@user_blueprint.route(rule="/user_info_by_id/<string:user_id>", methods=["POST"])
def user_info_by_id(user_id: str) -> Response:
    return jsonify(code=StatusCode.SUCCESS.value,
                   data=UserService.select_user_info_by_id(user_logic_object=user_logic_object, user_id=user_id))


@user_blueprint.route(rule="/user_count", methods=["GET"])
def user_count() -> Response:
    return jsonify(code=StatusCode.SUCCESS.value,
                   data=UserService.select_user_count(user_logic_object=user_logic_object))


@user_blueprint.route(rule="/now_user_info", methods=["GET"])
def now_user_info() -> Response:
    return jsonify(code=StatusCode.SUCCESS.value,
                   data=UserService.select_now_user_info(user_logic_object=user_logic_object))
