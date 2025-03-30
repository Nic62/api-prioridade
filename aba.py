import streamlit as st
import pandas as pd
import re
from datetime import datetime
import pytz

fuso_horario = pytz.timezone("America/Sao_Paulo")
st.set_page_config(
    page_title="Aba de Prioridades", 
    page_icon="https://logospng.org/download/grupo-caoa/logo-caoa-2048.png")

st.markdown(
      """
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            max-width: 400px;
            background: white;
            padding: 20px;
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
        .button-group button {
            background-color: #004080;
            color: white;
            border: none;
            padding: 10px 15px;
            margin: 5px;
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
col1, col2, col3 = st.columns(3)
with col2:
    st.image("https://logospng.org/download/grupo-caoa/logo-caoa-2048.png", width=200)
st.markdown("<h1 style='text-align: center;'>Prioridades</h1>", unsafe_allow_html=True)
st.divider()

st.header('Digite as informações abaixo:')

info_identificacao = st.text_input("Digite identificação:")
if info_identificacao and not re.match("^[A-Za-z.]+$", info_identificacao):
    st.error("Erro: Apenas letras (sem acentos) e ponto são permitidos!")

id_peca = st.text_input("Digite a peça:")
info_prio = st.radio("Selecione o grau de prioridade:", ['Por volta de 40 unidades', 'Menos de 20 unidades', 'Sem saldo no módulo'])

if "dados" not in st.session_state:
    st.session_state["dados"] = []
    
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Priorizar"):
        if info_identificacao and id_peca:
            agora = datetime.now(fuso_horario)
            novo_dado = {
                "Identificação": info_identificacao,
                "Peça": id_peca,
                "Prioridade": info_prio,
                "Data": agora.strftime("%Y-%m-%d"),
                "Hora": agora.strftime("%H:%M:%S")
            }
            
            st.session_state["dados"].append(novo_dado)
            st.session_state["mostrar_botao"] = True
            st.success("Peça priorizada com sucesso!")
        else:
            st.warning("Preencha todos os campos antes de priorizar!")

if st.session_state["dados"]:
    st.subheader("Prioridades Concluídas")
    df = pd.DataFrame(st.session_state["dados"])
    st.dataframe(df)

col1, col2, col3 = st.columns(3)
with col2:
    st.link_button("Planilha", "https://docs.google.com/spreadsheets/d/1jbI9wN9ny8HCJPOX66i69zdCSp6eoHNK9V5IhJ5ftMk/edit?gid=0#gid=0")
    
col1, col2, col3 = st.columns(3)
with col2:
    st.link_button("Dashboard", "https://lookerstudio.google.com/")

st.markdown("</div>", unsafe_allow_html=True)
