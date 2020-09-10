from fastapi import APIRouter,Depends
from auth import Auth

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/users/me", tags=["users"])
async def read_user_me(token: str = Depends(Auth.token_is_true)):
    return {"username": "fakecurrentuser"}


