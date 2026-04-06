from fastapi import APIRouter, Path
router = APIRouter()
@router.get("/")
def inicio():
    return {"Saludo": "Hola mundo con fastAPI"}

#peticion con parametros en la ruta (PATH)
#http://localhost:8000/suma1/10/20 
@router.get("/suma1/{num1}/{num2}") 
def suma1(num1:int, num2:int):
    suma = int(num1) + int(num2)
    return {"suma": f"{suma}"}

#peticion con parametros (QUERY)
#http://localhost:8000/suma2?num1=10&num2=20
@router.get("/suma2")
def suma(num1, num2): 
    suma = int(num1) + int(num2)
    return {"suma": f"{suma}"}

#peticion con parametros (PATH) y validacion de tipos 
#http://localhost:8000/saludo1/Einstein/50 
@router.get("/saludo1/{nombre}/{edad}")
def saludo(nombre: str, edad: int):
    frase = f"Tu nombre es: {nombre}, tienes {edad} años"
    return {"frase": f"{frase}"}

#peticion con parametros (QUERY) y validacion de tipos
#http://localhost:8000/saludo2?nombre=Newton&edad=70
@router.get("/saludo2")
def saludo2(nombre: str, edad:int): 
    frase= f"Su nombre es: {nombre}, tiene {edad} años"
    return {"frase": f"{frase}"}

#peticion con parametros (PATH) validacion de tipos y valor por default
#http://localhost:8000/frase1/buenos%20dias
#http://localhost:8000/frase1
#@router.get("/frase1")
#@router.get("/frase1/{saludo}")
#def frase1(saludo: str="Hola"):
 #   return {"saludo": f"{saludo}"}
router.get("/frase1")
def frase1():
    return {"saludo": "Hola"}
@router.get("/frase1/{saludo}")
def frase2(saludo: str):
    return {"saludo": f"{saludo}"}


#peticion con parametros (QUERY) validacion de tipos y valor por default
#http://localhost:8000/frase3?saludo=Buenas%20tardes
@router.get("/frase3")
def frase3(saludo: str = "Hola"):
    return {"saludo": f"{saludo}"}

#peticion con parametros (PATH) validacion de tipo y en los valores recibidos 
#Multiplicacion de 2 numero entre 1 y 10 
#http://localhost:8000/multiplicacion/5/8
#http://localhost:8000/multiplicacion/15/3  --> error
#http://localhost:8000/multiplicacion/1/7
@router.get("/multiplicacion/{num1}/{num2}", name="multiplicacion1_1_10")
def multiplicacion1 (
#El primer parametro indica el valor por default 
#El 2do parametro indica una regla 
#El 3er parametro indica otra regla
#El 4to parametro es un texto cuando se obtine un error y es para la decoumentacion 
#Reglas del 2do y 3er parametro 
#gt greater than (mayor que)
#ge greater equal (mayor o igual que)
#lit less than (menor que)
#le less equal (menor o igual que)
#multiple_of (multiplo de)
#min_length (longitud minima de caracteres)
#max_length (longitud maxima de caracteres)
#regex (expresion regular)
    num1: int = Path(..., gt=1, le=10, description="El primer numero debe estar entre 1 y 10"),
    num2: int = Path(..., gt=1, le=10, description="El segundo numero debe estar entre 1 y 10"),
):
    return {"multiplicacion": f"{num1 * num2}"}

#peticion con parametros (QUERY) validacion de tipo y en los valores recibidos
#multiplicar 2 numeros entre 1 y 10
#http://localhost:8000/multiplicacion2/5/3
#http://localhost:8000/multiplicacion2/15/3  --> error
#http://localhost:8000/multiplicacion2/2/3

@router.get("/multiplicacion2/{num1}/{num2}")
def multiplicacion2(
    num1: int = Path(..., gt=1, le=10, description="Primer número"),
    num2: int = Path(..., gt=1, le=10, description="Segundo número"),
):
    mult = num1 * num2
    return {"multiplicacion": mult}