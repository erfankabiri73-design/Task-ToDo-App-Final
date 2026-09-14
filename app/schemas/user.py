from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, ConfigDict
from core.exceptions import CustomValidationException
from messages.users import Messages


class RegisterSchema(BaseModel):
    email: EmailStr = Field(
        ...,
        examples=["john.doe@example.com"],
    )

    password: str = Field(
        ...,
        examples=["StrongPass123!"],
    )

    confirm_password: str = Field(
        ...,
        examples=["StrongPass123!"],
    )

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if len(value) < 5:
            raise CustomValidationException("Email must be at least 5 characters")

        if len(value) > 254:
            raise CustomValidationException("Email must not exceed 254 characters")

        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise CustomValidationException("Password must be at least 8 characters")

        if len(value) > 64:
            raise CustomValidationException("Password must not exceed 64 characters")

        if not any(char.islower() for char in value):
            raise CustomValidationException("Password must contain at least one lowercase letter")

        if not any(char.isupper() for char in value):
            raise CustomValidationException("Password must contain at least one uppercase letter")

        if not any(char.isdigit() for char in value):
            raise CustomValidationException("Password must contain at least one number")

        if not any(not char.isalnum() for char in value):
            raise CustomValidationException("Password must contain at least one special character")

        if any(char.isspace() for char in value):
            raise CustomValidationException("Password must not contain spaces")

        return value

    @field_validator("confirm_password")
    @classmethod
    def validate_confirm_password(cls, value):
        if len(value) < 8:
            raise CustomValidationException("Confirm password must be at least 8 characters")

        if len(value) > 64:
            raise CustomValidationException("Confirm password must not exceed 64 characters")

        return value

    @model_validator(mode="after")
    def check_passwords(self):
        if self.password != self.confirm_password:
            raise CustomValidationException(Messages.passwords_not_even)

        return self

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "john.doe@example.com",
                "password": "StrongPass123!",
                "confirm_password": "StrongPass123!"
            }
        }
    }



class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, examples=["a/@1234567"])
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "email": "user@example.com",
                    "password": "StrongPass@123",                    
                }
            ]
        }
    )
class LoginResponseSchema(BaseModel):
    user_id: int 
    email: str 
    type: str 
    detail: str 