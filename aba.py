import streamlit as st
import pandas as pd
import re
from datetime import datetime
import pytz

# Configuração do fuso horário
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Configuração da página
st.set_page_config(
    page_title="REGISTRADOR DE PRIORIDADE", 
    page_icon="https://logospng.org/download/grupo-caoa/logo-caoa-2048.png",
    layout="wide"
)

# Aplicando estilos personalizados para cobrir toda a tela com borda e sombra
st.markdown(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f4f4f4;
        }
        .stApp {
            border: 5px solid #004080;
            border-radius: 15px;
            box-shadow: 10px 10px 30px rgba(0, 0, 0, 0.3);
            padding: 20px;
            margin: 20px;
            background-color: white;
            width: calc(100vw - 40px);
            height: calc(100vh - 40px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        h2 {
            color: #004080;
            text-align: center;
        }
        .stTextInput, .stButton {
            width: 80%;
            margin: 10px auto;
        }
        .button-group {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .button-group button {
            background-color: #004080;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button-group button:hover {
            background-color: #002D5A;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo no topo
st.image("https://logospng.org/download/grupo-caoa/logo-caoa-2048.png", width=200)

# Título
st.markdown("<h2>Registro de Pedidos</h2>", unsafe_allow_html=True)

# Formulário
st.text_input("Usuário:", key="Nome")
st.text_input("Código da Peça:", key="Codigo")

# Botões
col1, col2 = st.columns(2)
with col1:
    if st.button("Registrar Pedido"):
        st.success("Pedido registrado com sucesso!")
with col2:
    if st.button("Lista de Pedidos"):
        st.markdown("[Ver Lista](https://docs.google.com/spreadsheets/d/1jbI9wN9ny8HCJPOX66i69zdCSp6eoHNK9V5IhJ5ftMk/edit?gid=0#gid=0)")
