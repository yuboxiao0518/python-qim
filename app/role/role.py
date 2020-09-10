from fastapi import APIRouter

router = APIRouter()


@router.get("/roles/", tags=["roles"])
async def read_roles():
    return [{"rolename": "Foo"}, {"rolename": "Bar"}]


@router.get("/roles/me", tags=["roles"])
async def read_role_me():
    return {"rolename": "fakecurrentuser"}
