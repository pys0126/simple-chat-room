from logic.chat_logic import ChatLogic


class ChatService:
    @classmethod
    def init_chat_logic(cls) -> ChatLogic:
        return ChatLogic()

    @staticmethod
    def select_message_list(chat_logic_object: ChatLogic) -> list:
        return chat_logic_object.select_message_list()
    
    @staticmethod
    def select_user_info_list(chat_logic_object: ChatLogic) -> list:
        return chat_logic_object.select_user_info_list()
    
    @staticmethod
    def select_user_info_by_id(chat_logic_object: ChatLogic, id: int) -> dict:
        return chat_logic_object.select_user_info_by_id(id=id)

    @staticmethod
    def select_user_count(chat_logic_object: ChatLogic) -> int:
        return chat_logic_object.select_user_count()