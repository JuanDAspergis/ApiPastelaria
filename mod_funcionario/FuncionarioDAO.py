from fastapi import APIRouter
router = APIRouter()

#Criando as os endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executando"}, 200

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": "get um executando"}, 200

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario():
    return {"msg": "post executado"}, 200

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 201