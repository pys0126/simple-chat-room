from config.status_code import StatusCode
from flask import Response, jsonify
import traceback


class CustomException(Exception):
    def __init__(self, message: str = "内部错误，请联系管理员", error_code: int = StatusCode.ERROR.value):
        self.message: str = message
        self.error_code: int = error_code


def exception_handle(exception: CustomException) -> Response:
    # 打印异常堆栈信息
    print(f"error_info => ", traceback.format_exc())
    response = jsonify(code=exception.error_code, message=exception.message)
    response.status_code = 500
    return response