<<<<<<< HEAD
=======
from fastapi import FastAPI, APIRouter,Request,Body
from fastapi.responses import JSONResponse
from schemas.user import RegisterSchema, LoginRequestSchema
from messages.users import Messages
>>>>>>> utill-error-handler-last-part

router = APIRouter()

@router.post("/register")
<<<<<<< HEAD

=======
def register(request: Request,
             Body : RegisterSchema
             ):
    return JSONResponse({"detail": Messages.registered_successfully})


@router.post("/login")
def login(request: Request,
             Body : LoginRequestSchema
             ):
    return JSONResponse({"detail": Messages.logedin_successfully})
>>>>>>> utill-error-handler-last-part

