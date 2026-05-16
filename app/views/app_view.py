import streamlit as st
import requests
import os

API_URL = "https://projeto-final-1-3srl.onrender.com"

st.set_page_config(page_title="Concessionria digital", layout="wide")

if "token" not in st.session_state:
    st.session_state.token = None

# --- AUTH ---
with st.sidebar:
    if not st.session_state.token:
        st.header("Login")
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            res = requests.post(f"{API_URL}/auth/login", json={"username": u, "password": p})
            if res.status_code == 200:
                st.session_state.token = res.json()["token"]
                st.rerun()
            else: st.error("Erro ao logar")
    else:
        st.success("Logado")
        if st.button("Sair"):
            st.session_state.token = None
            st.rerun()

# --- INTERFACE CRUD ---
st.title("Gestão de carros")

if st.session_state.token:
    # FORMULÁRIO DE CRIAÇÃO
    with st.expander("Novo Registro"):
        c1, c2, c3 = st.columns(3)
        tit = c1.text_input("Carro")
        aut = c2.text_input("Ano")
        das = c3.text_input("Cambio")
        if st.button("Salvar Livro"):
            requests.post(f"{API_URL}/Carros", json={"Carro": tit, "Ano": aut, "Cambio": das})
            st.toast("Pedido adicionado!")
            st.rerun()

    # LISTAGEM E AÇÕES
    livros = requests.get(f"{API_URL}/Livros").json()
    for l in livros:
        with st.container(border=True):
            col_info, col_del = st.columns([4, 1])
            col_info.write(f"**{l['Carro']}** | {l['Ano']}")
            if col_del.button("Excluir", key=f"del_{l['id']}"):
                requests.delete(f"{API_URL}/livros/{l['id']}")
                st.rerun()
else:
    st.info("Acesse com seu usuário para gerenciar os carros.")
