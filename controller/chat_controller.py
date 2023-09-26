from logic.chat_logic import ChatLogic
from config.status_code import StatusCode
from service.chat_service import ChatService
from flask import Blueprint, jsonify, Response

chat_blueprint: Blueprint = Blueprint("chat", __name__)
chat_logic_object: ChatLogic = ChatService.init_chat_logic()


@chat_blueprint.route(rule="/message_list", methods=["GET"])
def message_list() -> Response:
    return jsonify(code=StatusCode.SUCCESS.value,
                   data=ChatService.select_message_list(chat_logic_object=chat_logic_object)
                   )
