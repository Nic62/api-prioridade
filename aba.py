import streamlit as st
import pandas as pd
import re
# import joblib as jb
#.\venv\Scripts\activate
# streamlit run aba.py
st.set_page_config(
    page_title="Aba de Prioridades", 
    page_icon="https://logospng.org/download/grupo-caoa/logo-caoa-2048.png"
)

col1, col2 = st.columns([0.85, 0.15])

with col1:
    st.title("Prioridades")

with col2:
    st.image("https://logospng.org/download/grupo-caoa/logo-caoa-2048.png", width=120)  # Imagem ao lado

st.divider()
st.header('Digite as informações abaixo:')
info_identificacao = st.text_input("Digite identificação:")
if info_identificacao and not re.match("^[A-Za-z.]+$", info_identificacao):
    st.error("Erro: Apenas letras (sem acentos) e ponto são permitidos!")

id_peca = st.text_input("Digite a peça:")
info_prio = st.radio("Selecione o grau de prioridade:", ['Por volta de 40 unidades', 'Menos de 20 unidades', 'Sem saldo no módulo'])

# armazenamento
if "dados" not in st.session_state:
    st.session_state["dados"] = []

# Botão 1
if st.button("Priorizar"):
    if info_identificacao and id_peca:
        novo_dado = {"Identificação": info_identificacao, "Peça": id_peca, "Prioridade": info_prio}
        st.session_state["dados"].append(novo_dado)
        st.success("Peça priorizada com sucesso!")
    else:
        st.warning("Preencha todos os campos antes de priorizar!")

# Tabela
if st.session_state["dados"]:
    st.subheader("Prioridades Concluídas")
    df = pd.DataFrame(st.session_state["dados"])
    st.dataframe(df)
