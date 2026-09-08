from fastapi import FastAPI, APIRouter,Request,Body
from fastapi.responses import JSONResponse
from schemas.user import RegisterSchema, LoginRequestSchema
from messages.users import Messages

router = APIRouter()

@router.post("/register")
def register(request: Request,
             Body : RegisterSchema
             ):
    return JSONResponse({"detail": Messages.registered_successfully})


@router.post("/login")
def login(request: Request,
             Body : LoginRequestSchema
             ):
    return JSONResponse({"detail": Messages.logedin_successfully})

