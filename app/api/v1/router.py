from fastapi import APIRouter

from app.api.v1.users import router as users_router
from app.api.v1.todos import router as todos_router


router = APIRouter()

router.include_router(users_router)
router.include_router(todos_router)