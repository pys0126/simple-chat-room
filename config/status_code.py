from enum import Enum


class StatusCode(Enum):
    SUCCESS = 2000
    ERROR = 5000
    NOTFOUND = 4040
    LOGIN_ERROR = 4030
    REGISTER_ERROR = 4031
    ACCESS_DENIED = 4090
