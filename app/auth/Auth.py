from fastapi import HTTPException, Header
from config import config_util
import hmac


def get_sign() -> str:
    return config_util.get_value('signature','signature')


async def token_is_true(signature: str = Header(..., description="signature验证")):
    """签名验证，全局使用,验证失败就会报错"""
    compare_res = hmac.compare_digest(signature, get_sign())
    if not compare_res:
        raise HTTPException(
            status_code=401,
            detail="signature is fail",
            headers={"X-Error": "There goes my error"},
        )
    else:
        return {"flag": True}  # 可以自定義返回值，比如user或者其他的数据
