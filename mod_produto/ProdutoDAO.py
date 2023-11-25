import db
import security
from mod_produto.ProdutoModel import ProdutoDB
from mod_produto.Produto import Produto

from fastapi import Depends
from fastapi import APIRouter
router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

#Criando os endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.valor_unitario, corpo.foto)
        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.valor_unitario = corpo.valor_unitario
        dados.foto = corpo.foto

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try: 
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()