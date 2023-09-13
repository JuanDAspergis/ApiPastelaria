from pydantic import BaseModel

class Cliente(BaseModel):
        id_cliente: int = None
        nome: str
        cpf: str
        telefone: int
        compra_fiado: int = None
        dia_fiado: int
        senha: str = None