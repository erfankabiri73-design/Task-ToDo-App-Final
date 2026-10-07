import secrets
from fastapi import HTTPException, status

from app.repositories.user_repository import UserRepository
from app.schemas.user import RegisterSchema, LoginRequestSchema
from app.api.v1.auth import (
    generate_access_token,
    generate_refresh_token,
    decode_refresh_token,
)
from app.messages.users import Messages


class AccountService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register(self, request: RegisterSchema):
        existing_user = self.user_repo.get_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=Messages.user_already_exists,
            )

        self.user_repo.create_user(
            email=request.email,
            password=request.password,
        )

        return {
            "detail": Messages.registered_successfully
        }

    def login(self, request: LoginRequestSchema):
        user = self.user_repo.get_by_email(request.email)

        if not user or not user.verify_password(request.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=Messages.invalid_credentials,
            )

        access_token = generate_access_token(str(user.id))
        refresh_token = generate_refresh_token(str(user.id))
        csrf_token = secrets.token_urlsafe(32)

        return {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "csrf_token": csrf_token,
        }

    def refresh_access_token(self, refresh_token: str):
        user_id = decode_refresh_token(refresh_token)

        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=Messages.user_not_found,
            )

        return generate_access_token(str(user.id))