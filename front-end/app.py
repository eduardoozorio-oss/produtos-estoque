import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.title("Controle de Estoque")

menu = st.sidebar.selectbox("Menu", ["Listar", "Adicionar", "Atualizar", "Excluir", "Valor Total"])

# Listar
if menu == "Listar":
    st.subheader("Produtos cadastrados")
    r = requests.get(f"{API_URL}/produtos")
    df = pd.DataFrame(r.json())
    st.table(df)

