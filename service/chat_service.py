from logic.chat_logic import ChatLogic


class ChatService:
    @classmethod
    def init_chat_logic(cls) -> ChatLogic:
        return ChatLogic()

    @staticmethod
    def select_message_list(chat_logic_object: ChatLogic) -> list:
        return chat_logic_object.select_message_list()

    @staticmethod
    def message_count(chat_logic_object: ChatLogic) -> int:
        return chat_logic_object.select_message_count()
