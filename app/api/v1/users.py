from fastapi import FastAPI, APIRouter,Request,status,HTTPException,Depends
from fastapi.responses import JSONResponse
from models.user import UserModdel
from schemas.user import (
    RegisterSchema,
    LoginRequestSchema,
    LoginResponseSchema,
)
from auth import get_authenticated_user
from messages.users import Messages

router = APIRouter(    
    tags=["accounts"],
)

"""
def get_account_service(db: Session = Depends(get_db)) -> AccountService:
    user_repo = UserRepository(db)
    return AccountService(user_repo)
"""

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(request: RegisterSchema,
             ):
    return JSONResponse({"detail": Messages.registered_successfully})


@router.post("/login", status_code=status.HTTP_200_OK,)
def login(request: LoginRequestSchema,
             ):
    return JSONResponse({"detail": Messages.logged_in_successfully})

