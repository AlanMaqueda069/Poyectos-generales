from fastapi import Request #Entrega el url /objeto 
from fastapi.exceptions import RequestValidationError #Entrega el mensaje de error de validacion
from fastapi.responses import JSONResponse #prepara la respuesta en formato json

MENSAJE_ERROR ={
    "multiplicacion1_1_10": {
        "num1": {
            "less_than_equal": "El primer parametro debe ser menor a 10 ", 
            "greater_than_equal": "El primer parametro debe ser mayor a 1", 
            "int_parsting": "El primer poarametro debe ser unb numero", 
            "missing": "El primer parametro es obligatorio"
        },
        "num2": {
            "less_than_equal": "El segundo parametro debe ser menor a 10 ", 
            "greater_than_equal": "El segundo parametro debe ser mayor a 1", 
            "int_parsting": "El segundo poarametro debe ser unb numero", 
            "missing": "El segundo parametro es obligatorio"
        }
    }
}
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores =[]#Se prepara una lista para almacenar los errores
    ruta_obj= request.scope.get("route")#Obtiene la ruta del request
    ruta_name= getattr(ruta_obj, "name", None)#Entrega solo el atributo de la ruta y si no lo encuentra entrega None
    print (ruta_name)    
    print (exec.errors())
    for error in exc.errors(): 
        parametro = error ["loc"][-1]#Entrega el parametro que fallo 
        tipo_error= error ["type"]#Entrega el tipo de error [e]. greater_than_equal
        ruta_dicc= MENSAJE_ERROR.get(ruta_name)#Obtiene el diccionario de la ruta
        parametro_dicc= ruta_dicc.get(parametro)#Obtiene el diccionario del parametro
        mensaje_dicc=parametro_dicc.get(tipo_error,f"Error en el parametro {parametro}")#Obtiene el mensaje del tipo de error
        errores.append (mensaje_dicc)#Agrega el mensaje a la lista de errores
    return JSONResponse(
        status_code=422,
        content={"detalles": errores}
    )
#HACER LA VALIDACION PARA MULTIPLICAR 