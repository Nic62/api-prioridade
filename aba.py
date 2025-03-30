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

# Aplicando estilos personalizados para cobrir toda a tela
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 50%;
            max-width: 600px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h2 {
            color: #004080;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .button-group {
            display: flex;
            justify-content: space-around;
            margin-top: 15px;
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
    <div class='container'>
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

# Fechando a div principal
st.markdown("</div>", unsafe_allow_html=True)
