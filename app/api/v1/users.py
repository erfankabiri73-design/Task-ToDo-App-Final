from fastapi import FastAPI, APIRouter,Request,Body
from fastapi.responses import JSONResponse
from schemas.user import RegisterSchema
from messages.users import Messages

router = APIRouter()

@router.post("/register")
def register(request: Request,
             Body : RegisterSchema
             ):
    return JSONResponse({"detail": Messages.registered_successfully})


@router.post("/login")
def login():
    return "login"

