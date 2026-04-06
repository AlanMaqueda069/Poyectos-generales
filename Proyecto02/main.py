from fastapi import FastAPI
from routes import rutas
from fastapi.exceptions import RequestValidationError
from routes.core.exceptions import validation_exception_handler
    
app = FastAPI()
#Manejo de errores 
app.add_exception_handler(RequestValidationError, validation_exception_handler)
#rutas 
app.include_router(rutas.router) 