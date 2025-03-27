import streamlit as st
import pandas as pd
import re

# Configuração da página
st.set_page_config(
    page_title="Aba de Prioridades", 
    page_icon="🛠️"
)

# Criando layout com título e imagem ao lado
col1, col2 = st.columns([0.75, 0.25])  # Ajustei proporções para mais espaço à imagem

with col1:
    st.title("Prioridades")  # Título na esquerda

with col2:
    st.image("https://logospng.org/download/grupo-caoa/logo-caoa-2048.png", width=150)  # Imagem maior

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
