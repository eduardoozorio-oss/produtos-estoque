from fastapi import fastAPI


import funcao


#rodar o fastapi:
#python -m uvicorn api:app --reload


#testar api fastAPI
# /dcs > documentação Swagger
# /redoc > documentacao redoc
#
app = fastAPI(title ="controle de produtos e estoques")

@app.get("/")
def home():
    return {"mensagem": "bem-vindo ao controle de produtos e estoques"}









     












 
