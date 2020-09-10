from fastapi import APIRouter
import user.user as user_router
import role.role as role_router

#api路由
router = APIRouter()
router.include_router(
    user_router.router,
    prefix='/user',
    tags=['users']
)
router.include_router(
    role_router.router,
    prefix='/role',
    tags=['roles']
)
