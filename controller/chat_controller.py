from logic.chat_logic import ChatLogic
from config.status_code import StatusCode
from service.chat_service import ChatService
from flask import Blueprint, jsonify, Response


chat_blueprint: Blueprint = Blueprint("chat", __name__)
chat_logic_object: ChatLogic = ChatService.init_chat_logic()

@chat_blueprint.route(rule="/message_list", methods=["GET"])
def message_list() -> Response:
    return jsonify(code=StatusCode.SUCCESS, 
                   data=ChatService.select_message_list(chat_logic_object=chat_logic_object)
    )


@chat_blueprint.route(rule="/user_info_list", methods=["GET"])
def user_info_list() -> Response:
    return jsonify(code=StatusCode.SUCCESS, 
                   data=ChatService.select_user_info_list(chat_logic_object=chat_logic_object)
    )


@chat_blueprint.route(rule="/user_info_by_id/{int:id}", methods=["POST"])
def user_info_by_id(id: int) -> Response:
    return jsonify(code=StatusCode.SUCCESS, 
                   data=ChatService.select_user_info_by_id(chat_logic_object=chat_logic_object, id=id)
    )


@chat_blueprint.route(rule="/user_count", methods=["GET"])
def user_count() -> Response:
    return jsonify(code=StatusCode.SUCCESS, 
                   data=ChatService.select_user_count(chat_logic_object=chat_logic_object)
    )