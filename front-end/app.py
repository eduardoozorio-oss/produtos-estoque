import streamlit as st
import requests

#URL da API fastAPI
API_URL = "http://127.0.0.1:8000"


#Roda o streamlit 
# python -m streamlit run app.py
st.set_page_config(page_title="Controle de Produtos e Estoque", page_icon="")

#menu lateral
menu = st.sidebar.radio("", ["", ""])



























































# --- Adicionar Produto ---
st.subheader("Adicionar novo produto")
id = st.number_input("ID", min_value=1, step=1)
nome = st.text_input("Nome")
quantidade = st.number_input("Quantidade", min_value=0, step=1)
preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")

if st.button("Adicionar produto"):
    produto = {"id": id, "nome": nome, "quantidade": quantidade, "preco": preco}
    res = requests.post(f"{API_URL}/produtos", json=produto)
    if res.status_code == 200:
        st.success("Produto adicionado com sucesso!")
    else:
        st.error("Erro ao adicionar produto")

# --- Mostrar Estoque ---
st.subheader("Estoque Atual")
res = requests.get(f"{API_URL}/produtos")
if res.status_code == 200:
    produtos = res.json()
    if produtos:
        st.table(produtos)
        valor_total = sum(p["quantidade"] * p["preco"] for p in produtos)
        st.info(f"Valor total em estoque: R$ {valor_total:.2f}")
    else:
        st.write("Nenhum produto cadastrado ainda.")

# --- Atualizar Produto ---
st.subheader("Atualizar produto")
id_atualizar = st.number_input("ID do produto a atualizar", min_value=1, step=1)
nova_qtd = st.number_input("Nova quantidade (0 = não alterar)", min_value=0, step=1)
novo_preco = st.number_input("Novo preço (0 = não alterar)", min_value=0.0, format="%.2f")

if st.button("Atualizar"):
    params = {}
    if nova_qtd > 0:
        params["quantidade"] = nova_qtd
    if novo_preco > 0:
        params["preco"] = novo_preco
    if params:
        res = requests.put(f"{API_URL}/produtos/{id_atualizar}", params=params)
        if res.status_code == 200:
            st.success("Produto atualizado!")
        else:
            st.error("Produto não encontrado")
    else:
        st.warning("Preencha algum campo para atualizar.")

# --- Excluir Produto ---
st.subheader("Excluir produto")
id_excluir = st.number_input("ID do produto a excluir", min_value=1, step=1)
if st.button("Excluir"):
    res = requests.delete(f"{API_URL}/produtos/{id_excluir}")
    if res.status_code == 200:
        st.success("Produto removido!")
    else:
        st.error("Produto não encontrado")
