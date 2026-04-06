from uuid import UUID
from datetime import datetime,timezone
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from postgrest import CountMethod

def _table():
    sb=get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_table)
#Muestra una lista de productos de acuerdo a los parametros de paginacion
def list_products(limit:int=100,offset:int=0):
    try: 
        res=_table().select("*",count=CountMethod.exact).range(offset,offset+limit-1).execute()
        if not res.data:
            return {"items": [], "total": 0}
        return {"items":res.data or [],"total":res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error al mostrar los productos: {e}")
#Obtiene un producto por su ID 
def get_product(product_id:UUID):
    try:
        res=_table().select("*").eq("id",str(product_id)).execute()
        #encontrar con un limite
        #res=_table().select("*").eq("id",str(product_id)).limit(1).execute()
        if not res.data:
            raise HTTPException(status_code=404,detail=f"Producto no encontrado con el id {product_id}")
        return res.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error al obtener el producto: {e}")
    
def create_product(datos:dict):
    try:
        if not datos:
            raise HTTPException(status_code=404,detail=f"Error al crear el producto: No se proporcionaron datos")
        datos=jsonable_encoder(datos)
        res=_table().insert(datos).execute()
        return res.data[0] if res.data else None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error al crear el producto: {e}")
    
def update_product(product_id:UUID,datos:dict):
    try:
        if not datos or not product_id:
            raise HTTPException(status_code=404,detail=f"Error al actualizar el producto: No se proporcionaron datos o ID del producto")
        datos=jsonable_encoder(datos)
        res=_table().update(datos).eq("id",str(product_id)).execute()
        return res.data[0] if res.data else None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error al actualizar el producto: {e}")
    
def delete_product(product_id:UUID):
    try:
        if not product_id:
            raise HTTPException(status_code=404,detail=f"Error al eliminar el producto: No se proporcionó ID del producto")
        res=_table().delete().eq("id",str(product_id)).execute()
        return res.data[0] if res.data else None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error al eliminar el producto: {e}")