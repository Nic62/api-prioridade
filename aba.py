# import joblib as jb
#.\venv\Scripts\activate
# streamlit run aba.py
#  Local URL: http://localhost:8501
# Network URL: http://192.168.1.103:8501
import re
import streamlit as st
st.title("Aba de Prioridades")
st.divider()
st.header('Digite as informações abaixo:')
#----------------------------------
info_identidicacao=st.text_input("Digite identificação:", key="info_identidicacao")
st.write(f"Sua identificação: {info_identidicacao}")
if info_identidicacao and not re.match("^[A-Za-z.]+$", info_identidicacao):
    st.error("Erro: Apenas letras (sem acentos) e ponto são permitidos!")

info_quant = st.number_input("Digite a quantidade de peças",min_value=1,max_value=300)
st.write(f"Sua quantidade é: {info_quant}")

id_peca=st.text_input("Digite a peça:")
st.write(f"Sua peça é : {id_peca}",key="info_peca")

info_turno = st.radio("Selecione o turno?", ['Primeiro', 'Segundo','Terceiro'])
st.write(f"Seu turno: {info_turno}")