#Activar entorno virtual: .\env\Scripts\activate
#Crear entorno virtual: python -m venv env
#Salir del entorno virtual: deactivate
#Instalar el frmaework y el servidor : pip install fastapi uvicorn 
#Crear el archivo con todas las instalaciones : pip freeze > requirements.txt
#ejecutar la aplicacion: uvicorn main:app --reload
#documentacion progrmandores 
#/docs
#Documentacion administradores
#/redoc
from fastapi import FastAPI, Path, Query
app=FastAPI() #Crear el servidor de FastAPI
@app.get("/")#decorador para definir la ruta
@app.get("/home")#Cada funcion puede tener mas de una ruta 
def inicio():
    return {"Hello": "World"}#Generamos la salida como un diccionario

#peticion con parametros en la ruta 
#http://localhost:8000/suma1/10/20
@app.get("/suma1/{num1}/{num2}")
def suma1(num1:int, num2:int):
    suma = int(num1) + int(num2)
    return {"suma": f"{suma}"}

#peticion con parametros 
#http://localhost:8000/suma2?num1=10&num2=20
@app.get("/suma2")
def suma(num1, num2): 
    suma = int(num1) + int(num2)
    return {"suma": f"{suma}"}