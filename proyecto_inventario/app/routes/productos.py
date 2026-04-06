from fastapi import APIRouter,Path,Query
from uuid import UUID
from app.models.producto import ProductCreate,ProductUpdate,ProductOut,ProductList
from app.services.productos_service import list_products,get_product,create_product,update_product,delete_product

router=APIRouter(prefix="/productos")

@router.get("/",name="Listar_productos")
def listar_productos(limit:int=Query(default=100,ge=1,le=200),offset:int=Query(0,ge=0)):
    return list_products(limit,offset)

@router.get("/{product_id}",response_model=ProductOut,name="Obtener_producto")
def api_get_product(product_id:UUID=Path(...)):
    return get_product(product_id)

@router.post("/",response_model=ProductCreate,name="Crear_producto")
def api_create_product(body:ProductCreate):
    return create_product(body.model_dump())

@router.put("/{product_id}",response_model=ProductOut,name="Actualizar_producto")
def api_update_product(product_id:UUID,body:ProductUpdate):
    return update_product(product_id,body.model_dump(exclude_unset=True))

@router.delete("/{product_id}",name="Eliminar_producto")
def api_delete_product(product_id:UUID):
    return delete_product(product_id)
