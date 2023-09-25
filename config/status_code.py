from enum import Enum

class StatusCode(Enum):
    SUCCESS: int = 2000
    ERROR: int = 4000
    NOTFOUND: int = 4040
    LOGIN_ERROR: int = 4030