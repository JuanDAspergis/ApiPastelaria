from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    valor_unitario: str
    foto: str = None