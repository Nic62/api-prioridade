import streamlit as st
import pandas as pd
import re
from datetime import datetime


onedrive_link = "https://onedrive.live.com/download?cid=8388a7abc69fb78d&resid=8388A7ABC69FB78D%21123&authkey=ABC123"

st.set_page_config(page_title="Aba de Prioridades", page_icon="📋")

st.header('Digite as informações abaixo:')

info_identificacao = st.text_input("Digite identificação:")
if info_identificacao and not re.match("^[A-Za-z.]+$", info_identificacao):
    st.error("Erro: Apenas letras (sem acentos) e ponto são permitidos!")

id_peca = st.text_input("Digite a peça:")
info_prio = st.radio("Selecione o grau de prioridade:", ['Por volta de 40 unidades', 'Menos de 20 unidades', 'Sem saldo no módulo'])

if st.button("Priorizar"):
    if info_identificacao and id_peca:
        novo_dado = {
            "Identificação": info_identificacao,
            "Peça": id_peca,
            "Prioridade": info_prio,
            "Data e Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            df_existente = pd.read_excel(onedrive_link)
            df_final = pd.concat([df_existente, pd.DataFrame([novo_dado])], ignore_index=True)
        except:
            df_final = pd.DataFrame([novo_dado])
        
        df_final.to_excel("prioridades.xlsx", index=False)

        st.success("Peça priorizada com sucesso!")
    else:
        st.warning("Preencha todos os campos antes de priorizar!")

st.link_button("Acessar Planilha no OneDrive", onedrive_link)


if st.session_state["dados"]:
    st.subheader("Prioridades Concluídas")
    df = pd.DataFrame(st.session_state["dados"])
    st.dataframe(df)

st.link_button("Acessar Planilha", "")
st.link_button("Acessar BI", "https://docs.google.com/spreadsheets/d/1jbI9wN9ny8HCJPOX66i69zdCSp6eoHNK9V5IhJ5ftMk/edit?gid=0#gid=0")
