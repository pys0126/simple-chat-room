from logic.chat_logic import ChatLogic
from util.json_util import chat_decoder
from entity.chat_entity import ChatEntity
from config.status_code import StatusCode
from service.chat_service import ChatService
from flask import Blueprint, jsonify, Response, request

chat_blueprint: Blueprint = Blueprint("chat", __name__)
chat_logic_object: ChatLogic = ChatService.init_chat_logic()


@chat_blueprint.route(rule="/send_message", methods=["POST"])
def send_message() -> Response:
    chat_entity: ChatEntity = chat_decoder.decode(s=request.data.decode("u8"))
    ChatService.send_message(chat_logic_object=chat_logic_object, chat_entity=chat_entity)
    return jsonify(code=StatusCode.SUCCESS.value, message="成功")


@chat_blueprint.route(rule="/message_list", methods=["GET"])
def message_list() -> Response:
    return jsonify(code=StatusCode.SUCCESS.value,
                   data=ChatService.message_list(chat_logic_object=chat_logic_object))
