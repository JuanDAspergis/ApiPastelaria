from fastapi import APIRouter

router = APIRouter()

#Criar os endpoints do Cliente: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executando"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    return {"msg": "get um executando"}, 200

@router.post("/cliente/", tags=["Cliente"])
def post_cliente():
    return {"msg": "post executando"}, 200

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201