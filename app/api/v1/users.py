from fastapi import FastAPI, APIRouter,Request,status,HTTPException,Depends
from fastapi.responses import JSONResponse
from models.user import UserModdel 
from sqlalchemy.orm import Session
from core.database import get_db
from core.config import settings
from schemas.user import (
    RegisterSchema,
    LoginRequestSchema,
    LoginResponseSchema,
)
from repositories.user_repository import UserRepository
from services.auth_service import AccountService
from .auth import get_authenticated_user
from messages.users import Messages

router = APIRouter(    
    tags=["accounts"],
)


def get_account_service(db: Session = Depends(get_db)) -> AccountService:
    user_repo = UserRepository(db)
    return AccountService(user_repo)

"""
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(request: RegisterSchema,
             ):
    return JSONResponse({"detail": Messages.registered_successfully})
"""
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterSchema,
    service: AccountService = Depends(get_account_service),
):
    return service.register(request)

@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseSchema,
)
async def login(
    request: LoginRequestSchema,
    service: AccountService = Depends(get_account_service),
):
    result = service.login(request)

    user = result["user"]

    response = JSONResponse(
        {
            "user_id": user.id,
            "email": user.email,
            "type": user.type,
            "detail": Messages.logged_in_successfully,
        },
        status_code=status.HTTP_200_OK,
    )

    response.set_cookie(
        "access_token",
        result["access_token"],
        httponly=settings.AUTH_COOKIE_HTTPONLY,
        secure=settings.AUTH_COOKIE_SECURE,
        samesite=settings.AUTH_COOKIE_SAMESITE,
    )

    response.set_cookie(
        "refresh_token",
        result["refresh_token"],
        httponly=settings.AUTH_COOKIE_HTTPONLY,
        secure=settings.AUTH_COOKIE_SECURE,
        samesite=settings.AUTH_COOKIE_SAMESITE,
    )

    return response


"""
def login(request: LoginRequestSchema,
             ):
    return JSONResponse({"detail": Messages.logged_in_successfully})
"""



@router.post("/refresh-token")
async def refresh_token(
    request: Request,
    service: AccountService = Depends(get_account_service),
):
    token = request.cookies.get("refresh_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=Messages.refresh_token_not_found,
        )

    new_access_token = service.refresh_access_token(token)

    response = JSONResponse(
        {"detail": Messages.token_refreshed_successfully},
        status_code=status.HTTP_200_OK,
    )

    response.set_cookie(
        "access_token",
        new_access_token,
        httponly=settings.AUTH_COOKIE_HTTPONLY,
        secure=settings.AUTH_COOKIE_SECURE,
        samesite=settings.AUTH_COOKIE_SAMESITE,
    )

    return response






@router.get("/me")
async def session_verify(
    current_user: UserModdel = Depends(get_authenticated_user),
):
    return JSONResponse({
        "is_authenticated": True,
        "user": {
            "id": current_user.id,
            "email": current_user.email,
            "username": current_user.username,
            "type": current_user.type,
        },
    })



