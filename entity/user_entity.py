from util.string_util import create_uuid


class UserEntity:
    def __init__(self, user_id: str = create_uuid(), username: str = None, nikename: str = None, password: str = None):
        self.user_id: str = user_id
        self.nikename: str = nikename
        self.username: str = username
        self.password: str = password