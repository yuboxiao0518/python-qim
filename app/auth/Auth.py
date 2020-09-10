from fastapi import HTTPException, Header
from config import config_util


def get_sign() -> str:
    return '123'


async def token_is_true(token: str = Header(..., description="token验证")):
    """签名验证，全局使用,验证失败就会报错"""
    if token != get_sign():
        raise HTTPException(
            status_code=401,
            detail="token is fail",
            headers={"X-Error": "There goes my error"},
        )
    else:
        return {"token": token}  # 可以自定義返回值，比如user或者其他的数据
