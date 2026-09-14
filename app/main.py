from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
# route import
<<<<<<< HEAD
from api.v1.users import APIRouter
from utils.exceptions import (http_exception_handler,
=======
from api.v1.users import router

from core.exceptions import (http_exception_handler,
>>>>>>> utill-error-handler-last-part
                              validation_exception_handler,
                              unhandled_exception_handler)
app = FastAPI()

<<<<<<< HEAD
=======

>>>>>>> utill-error-handler-last-part
app.add_exception_handler(HTTPException,http_exception_handler)
app.add_exception_handler(RequestValidationError,validation_exception_handler)
app.add_exception_handler(Exception,unhandled_exception_handler)

# include route
<<<<<<< HEAD
app.include_router(APIRouter)
=======
app.include_router(router)
>>>>>>> utill-error-handler-last-part
