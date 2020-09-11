from fastapi import APIRouter, Depends
from auth import Auth
import repository.OracleRepository as dao

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    dao1 = dao.OracleRepository()
    sql_select = ''' SELECT * from META_MODEL'''
    select = dao1.select(sql_select)
    return select


@router.get("/users/me", tags=["users"])
async def read_user_me(token: str = Depends(Auth.token_is_true)):
    return {"username": "fakecurrentuser"}
