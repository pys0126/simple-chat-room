from logic.chat_logic import ChatLogic
from entity.chat_entity import ChatEntity


class ChatService:
    @classmethod
    def init_chat_logic(cls) -> ChatLogic:
        return ChatLogic()

    @staticmethod
    def send_message(chat_logic_object: ChatLogic, chat_entity: ChatEntity) -> None:
        chat_logic_object.send_message(chat_entity=chat_entity)

    @staticmethod
    def message_list(chat_logic_object: ChatLogic) -> list:
        return chat_logic_object.select_message_list()

    @staticmethod
    def message_count(chat_logic_object: ChatLogic) -> int:
        return chat_logic_object.select_message_count()
