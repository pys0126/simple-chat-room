class ChatEntity:
    def __init__(self, user_id: str, content: str):
        self.user_id: str = user_id
        self.content: str = content