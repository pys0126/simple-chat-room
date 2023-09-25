from logic.user_logic import UserLogic


class UserService:
    @classmethod
    def init_user_logic(cls) -> UserLogic:
        return UserLogic()

    @staticmethod
    def login(user_logic_object: UserLogic, username: str, password: str) -> None:
        ...
    
    @staticmethod
    def register(user_logic_object: UserLogic, username: str, nikename: str, password: str) -> None:
        ...