from fastapi import Request  # entrega el url
from fastapi.exceptions import RequestValidationError  # mensaje de error de validacion
from fastapi.responses import JSONResponse  # preparar la respuesta en json

MENSAJES_ERROR={
    "multiplicacion1_1_10":{
        "num1":{
            "less_than_equal":"El num1 debe ser menor o igual a 10",
            "greater_than_equal":"El num1 debe ser mayor o igual a 1",
            "int_parsing":"El num1 debe ser un numero entero",
            "missing":"El num1 es obligatorio"
        },
        "num2":{
            "less_than_equal":"El num2 debe ser menor o igual a 10",
            "greater_than_equal":"El num2 debe ser mayor o igual a 1",
            "int_parsing":"El num2 debe ser un numero entero",
            "missing":"El num2 es obligatorio"
        }
    },
    "Obtener producto por ID":{
        "product_id":{
            "uuid_parsing":"El ID del producto debe ser un UUID válido",
            "missing":"El ID del producto es obligatorio"
        }
    },
    "Crear nuevo producto":{
        "name":{
            "string_too_short":"El nombre debe tener al menos 1 carácter",
            "string_too_long":"El nombre no puede exceder 200 caracteres",
            "missing":"El nombre es obligatorio"
        },
        "quantity":{
            "greater_than_equal":"La cantidad debe ser mayor o igual a 1",
            "int_parsing":"La cantidad debe ser un número entero",
            "missing":"La cantidad es obligatoria"
        },
        "ingreso_date":{
            "date_parsing":"La fecha de ingreso debe ser una fecha válida",
            "missing":"La fecha de ingreso es obligatoria"
        },
        "min_stock":{
            "greater_than_equal":"El stock mínimo debe ser mayor o igual a 0",
            "int_parsing":"El stock mínimo debe ser un número entero",
            "missing":"El stock mínimo es obligatorio"
        },
        "max_stock":{
            "greater_than_equal":"El stock máximo debe ser mayor o igual a 0",
            "less_than_equal":"El stock máximo no puede exceder 1000",
            "int_parsing":"El stock máximo debe ser un número entero",
            "missing":"El stock máximo es obligatorio"
        }
    },
    "Actualizar producto por ID":{
        "product_id":{
            "uuid_parsing":"El ID del producto debe ser un UUID válido",
            "missing":"El ID del producto es obligatorio"
        },
        "name":{
            "string_too_short":"El nombre debe tener al menos 1 carácter",
            "string_too_long":"El nombre no puede exceder 200 caracteres"
        },
        "quantity":{
            "greater_than_equal":"La cantidad debe ser mayor o igual a 1",
            "int_parsing":"La cantidad debe ser un número entero"
        },
        "ingreso_date":{
            "date_parsing":"La fecha de ingreso debe ser una fecha válida"
        },
        "min_stock":{
            "greater_than_equal":"El stock mínimo debe ser mayor o igual a 0",
            "int_parsing":"El stock mínimo debe ser un número entero"
        },
        "max_stock":{
            "greater_than_equal":"El stock máximo debe ser mayor o igual a 0",
            "less_than_equal":"El stock máximo no puede exceder 1000",
            "int_parsing":"El stock máximo debe ser un número entero"
        }
    },
    "Eliminar producto por ID":{
        "product_id":{
            "uuid_parsing":"El ID del producto debe ser un UUID válido",
            "missing":"El ID del producto es obligatorio"
        }
    },
    "Listar_productos":{
        "limit":{
            "greater_than_equal":"El parámetro limit debe ser mayor o igual a 1.",
            "less_than_equal":"El parámetro limit debe ser menor o igual a 200.",
            "int_parsing":"El parámetro limit debe ser un número entero."
        },
        "offset":{
            "greater_than_equal":"El parámetro offset debe ser mayor o igual a 0.",
            "int_parsing":"El parámetro offset debe ser un número entero."
        }
    }
}


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = []  # se prepara una lista vacia para guardar los errores
    ruta_obj = request.scope.get("route")  # obtiene la ruta del request
    ruta_name = getattr(
        ruta_obj, "name", ""
    )  # obtiene el atributo name de la ruta y si no lo encuentra devuelve vacio

    for error in exc.errors():  # recorre la lista de errores
        parametro = error.get("loc")[-1]  # nombre del parametro con error
        tipo = error.get("type", "")  # tipo de error
        ruta_dicc = MENSAJES_ERROR.get(ruta_name, {})  # diccionario por ruta
        parametro_dicc = ruta_dicc.get(parametro, {})  # diccionario por parametro
        mensaje_dicc = parametro_dicc.get(tipo, error.get("msg", "Error de validacion"))
        errores.append(mensaje_dicc)

    return JSONResponse(status_code=422, content={"detalles": errores})
