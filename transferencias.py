import streamlit as st
import pandas as pd
# streamlit run solicitacao.py



# Configuração da página
st.set_page_config(
    page_title="Aba de logistica", 
    page_icon="https://logospng.org/download/grupo-caoa/logo-caoa-2048.png"
)

# Imagem centralizada
st.markdown(
    "<div style='text-align: center;'><img src='https://logospng.org/download/grupo-caoa/logo-caoa-2048.png' width='150'></div>",
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align: center;'>Picking by Light</h1>", 
    unsafe_allow_html=True
)

# Gerenciar estado da seção ativa
if "active_section" not in st.session_state:
    st.session_state.active_section = None

# Função para mostrar a seção
def show_section(section):
    st.session_state.active_section = section

# Função para mostrar o botão de voltar
def voltar():
    st.session_state.active_section = None

# Botões para ativar seções
if st.session_state.active_section is None:
    st.divider()
    st.header("Escolha a ação desejada:")
    
    if st.button("Solicitação"):
        show_section("Solicitação")
    if st.button("Endereçamento"):
        show_section("Endereçamento")
    if st.button("Transferência"):
        show_section("Transferência")

# Solicitação
if st.session_state.active_section == "Solicitação":
    st.subheader("Área para Solicitação")
    usuario = st.text_input("Usuário", key="solicitacao_usuario")
    part_number = st.text_input("Part number", key="solicitacao_part_number")
    quantidade = st.number_input("Quantidade", min_value=1, key="solicitacao_quantidade")
    if st.button("Confirmar Solicitação", key="solicitacao_confirmar"):
        st.success(f"Solicitação enviada! Usuário: {usuario}, Produto: {part_number}, Quantidade: {quantidade}")
        # Registra a solicitação
        if "solicitacoes" not in st.session_state:
            st.session_state["solicitacoes"] = []
        st.session_state["solicitacoes"].append({"Usuário": usuario, "Produto": part_number, "Quantidade": quantidade})
    
    if st.session_state.get("solicitacoes"):
        st.subheader("Solicitações Realizadas")
        df = pd.DataFrame(st.session_state["solicitacoes"])
        st.dataframe(df)
    
    if st.button("Voltar"):
        voltar()

# Endereçamento
if st.session_state.active_section == "Endereçamento":
    st.subheader("Área para Endereçamento")
    usuario = st.text_input("Usuário", key="enderecamento_usuario")
    indexador = st.text_input("Indexador", key="enderecamento_indexador")
    modulo = st.text_input("Módulo", key="enderecamento_modulo")
    quantidade = st.number_input("Quantidade", min_value=1, key="enderecamento_quantidade")
    if st.button("Confirmar Endereçamento", key="enderecamento_confirmar"):
        st.success(f"Endereçamento confirmado! Usuário: {usuario}, Indexador: {indexador}, Módulo: {modulo}, Quantidade: {quantidade}")
        # Registra o endereçamento
        if "enderecamentos" not in st.session_state:
            st.session_state["enderecamentos"] = []
        st.session_state["enderecamentos"].append({"Usuário": usuario, "Indexador": indexador, "Módulo": modulo, "Quantidade": quantidade})
    
    if st.session_state.get("enderecamentos"):
        st.subheader("Endereçamentos Realizados")
        df = pd.DataFrame(st.session_state["enderecamentos"])
        st.dataframe(df)
    
    if st.button("Voltar"):
        voltar()

# Transferência
if st.session_state.active_section == "Transferência":
    st.subheader("Área para Transferência")
    usuario = st.text_input("Usuário", key="transferencia_usuario")
    codigo = st.text_input("Código", key="transferencia_codigo")
    modulo = st.text_input("Módulo", key="transferencia_modulo")
    if st.button("Confirmar Transferência", key="transferencia_confirmar"):
        st.success(f"Transferência confirmada! Usuário: {usuario}, Código: {codigo}, Módulo: {modulo}")
        # Registra a transferência
        if "transferencias" not in st.session_state:
            st.session_state["transferencias"] = []
        st.session_state["transferencias"].append({"Usuário": usuario, "Código": codigo, "Módulo": modulo})
    
    if st.session_state.get("transferencias"):
        st.subheader("Transferências Realizadas")
        df = pd.DataFrame(st.session_state["transferencias"])
        st.dataframe(df)
    
    if st.button("Voltar"):
        voltar()
