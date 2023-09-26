from uuid import uuid4
import hashlib


def create_uuid() -> str:
    return str(uuid4())


def calculate_md5(text: str) -> str:
    # 创建 MD5 对象
    md5 = hashlib.md5()
    # 更新哈希对象以包含字符串的字节表示
    md5.update(text.encode("utf-8"))
    # 计算并返回哈希值的十六进制表示
    return md5.hexdigest()