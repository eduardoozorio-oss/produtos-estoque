from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    categoria: Optional[str] = None
    preco: float
    quantidade: int

class ProdutoUpdate(BaseModel):
    preco: Optional[float] = None
    quantidade: Optional[int] = None

class Produto(ProdutoBase):
    id: int
    class Config:
        orm_mode = True
