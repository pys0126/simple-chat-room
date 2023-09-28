from logic.user_logic import UserLogic
from entity.user_entity import UserEntity


class UserService:
    @classmethod
    def init_user_logic(cls) -> UserLogic:
        return UserLogic()

    @staticmethod
    def login(user_logic_object: UserLogic, user_entity: UserEntity) -> dict:
        return user_logic_object.login(user_entity=user_entity)

    @staticmethod
    def register(user_logic_object: UserLogic, user_entity: UserEntity) -> None:
        user_logic_object.register(user_entity=user_entity)

    @staticmethod
    def logout(user_logic_object: UserLogic, user_id: str) -> None:
        user_logic_object.logout(user_id=user_id)

    @staticmethod
    def select_user_info_list(user_logic_object: UserLogic) -> list:
        return user_logic_object.select_user_info_list()

    @staticmethod
    def select_user_info_by_id(user_logic_object: UserLogic, user_id: str) -> dict:
        return user_logic_object.select_user_info_by_id(user_id=user_id)

    @staticmethod
    def select_user_count(user_logic_object: UserLogic) -> int:
        return user_logic_object.select_user_count()
