import streamlit as st

# Gerenciar estado da seção ativa
if "active_section" not in st.session_state:
    st.session_state.active_section = None

# Funções
def show_section(section):
    st.session_state.active_section = section

# Botões para ativar seções
if st.session_state.active_section is None:
    st.title("Picking by Light")
    st.divider()
    st.header("Escolha a ação desejada:")
    
    if st.button("Solicitação"):
        show_section("Solicitação")
    if st.button("Endereçamento"):
        show_section("Endereçamento")
    if st.button("Transferência"):
        show_section("Transferência")
    if st.button("Semi prioridade"):
        show_section("Semi prioridade")

# Solicitação
if st.session_state.active_section == "Solicitação":
    st.subheader("Área para Solicitação")
    part_number = st.text_input("Part number", key="solicitacao_part_number")
    quantidade = st.number_input("Quantidade", min_value=1, key="solicitacao_quantidade")
    prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"], key="solicitacao_prioridade")
    if st.button("Confirmar Solicitação", key="solicitacao_confirmar"):
        st.success(f"Solicitação enviada! Produto: {part_number}, Quantidade: {quantidade}, Prioridade: {prioridade}")

# Endereçamento
if st.session_state.active_section == "Endereçamento":
    st.subheader("Área para Endereçamento")
    part_number = st.text_input("Part number", key="enderecamento_part_number")
    modulo = st.text_input("Módulo", key="enderecamento_modulo")
    quantidade = st.number_input("Quantidade", min_value=1, key="enderecamento_quantidade")
    if st.button("Confirmar Endereçamento", key="enderecamento_confirmar"):
        st.success(f"Endereçamento confirmado! Part Number: {part_number}, Módulo: {modulo}, Quantidade: {quantidade}")

# Transferência
if st.session_state.active_section == "Transferência":
    st.subheader("Área para Transferência")
    codigo = st.text_input("Código", key="transferencia_codigo")
    modulo = st.text_input("Módulo", key="transferencia_modulo")
    if st.button("Confirmar Transferência", key="transferencia_confirmar"):
        st.success(f"Transferência confirmada! Código: {codigo}, Módulo: {modulo}")

# Semi Prioridade
if st.session_state.active_section == "Semi prioridade":
    st.subheader("Área para Semi Prioridade")
    prioridade = st.selectbox("Escolha a Semi Prioridade", ["Alta", "Média", "Baixa"], key="semi_prioridade")
    if st.button("Confirmar Semi Prioridade", key="semi_prioridade_confirmar"):
        st.success(f"Semi Prioridade escolhida: {prioridade}")
