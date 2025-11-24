from fastapi import FastAPI
import crud
from schemas import ProdutoBase, ProdutoUpdate

app = FastAPI(title="API Controle de Estoque")

@app.post("/produtos")
def adicionar_produto(produto: ProdutoBase):
    return crud.criar_produto(produto)

@app.get("/produtos")
def listar():
    return crud.listar_produtos()

@app.put("/produtos/{id}")
def atualizar(id: int, produto: ProdutoUpdate):
    return crud.atualizar_produto(id, produto)

@app.delete("/produtos/{id}")
def deletar(id: int):
    return crud.excluir_produto(id)
