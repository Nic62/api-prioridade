import streamlit as st
import pandas as pd
import re
# import joblib as jb
#.\venv\Scripts\activate
# streamlit run aba.py
#  Local URL: http://localhost:8501
# Network URL: http://192.168.1.103:8501
# Configuração da página
st.set_page_config(
    page_title="Aba de Prioridades", 
    page_icon="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAsJCQcJCQcJCQkJCwkJCQkJCQsJCwsMCwsLDA0QDBEODQ4MEhkSJRodJR0ZHxwpKRYlNzU2GioyPi0pMBk7IRP/2wBDAQcICAsJCxULCxUsHRkdLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCz/wAARCAC0ALIDASIAAhEBAxEB/8QAHAABAAIDAQEBAAAAAAAAAAAAAAEHBAYIBQID/8QAQhAAAQQBAQUGAwUFAw0AAAAAAQACAwQFEQYHEhI..."
)

# Título com imagem ao lado
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h1 style="margin-right: 10px;">Prioridades</h1>
        <img src="https://logospng.org/download/grupo-caoa/logo-caoa-2048.png" width="50">
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.header('Digite as informações abaixo:')

# Entrada de dados
info_identificacao = st.text_input("Digite identificação:")
if info_identificacao and not re.match("^[A-Za-z.]+$", info_identificacao):
    st.error("Erro: Apenas letras (sem acentos) e ponto são permitidos!")

id_peca = st.text_input("Digite a peça:")
info_prio = st.radio("Selecione o grau de prioridade:", ['Por volta de 40 unidades', 'Menos de 20 unidades', 'Sem saldo no módulo'])

# Lista para armazenar dados temporários
if "dados" not in st.session_state:
    st.session_state["dados"] = []

# Botão para adicionar os dados
if st.button("Priorizar"):
    if info_identificacao and id_peca:
        novo_dado = {"Identificação": info_identificacao, "Peça": id_peca, "Prioridade": info_prio}
        st.session_state["dados"].append(novo_dado)
        st.success("Peça priorizada com sucesso!")
    else:
        st.warning("Preencha todos os campos antes de priorizar!")

# Exibir tabela com os dados
if st.session_state["dados"]:
    st.subheader("Prioridades Concluídas")
    df = pd.DataFrame(st.session_state["dados"])
    st.dataframe(df)
