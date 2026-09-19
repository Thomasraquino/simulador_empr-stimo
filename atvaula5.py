import streamlit as st

st.set_page_config(page_title="Simulador de Crédito - Moto", page_icon="🏍️")

st.title("🏍️ Análise de Crédito - Financiamento de Moto")
st.write("Preencha os dados abaixo para verificar a liberação do seu crédito.")

with st.form("form_credito"):
    idade = st.number_input("Idade (anos)", min_value=0, max_value=100, value=20, step=1)
    renda = st.number_input("Renda Mensal (R$)", min_value=0.0, value=2500.00, step=100.00, format="%.2f")
    parcela = st.number_input("Valor da Parcela Desejada (R$)", min_value=0.0, value=850.00, step=50.00, format="%.2f")
    
    submeter = st.form_submit_button("Analisar Crédito", type="primary")

if submeter:
    st.divider()
    
    if renda <= 0 or parcela <= 0:
        st.warning("Informe valores válidos para renda e parcela.")
    elif idade < 18:
        st.error("❌ Crédito Negado: É necessário ter no mínimo 18 anos completos.")
    else:
        parcela_maxima = renda * 0.30
        percentual = (parcela / renda) * 100

        if parcela > parcela_maxima:
            st.error("❌ Crédito Negado: O valor da parcela ultrapassa o limite de 30% da sua renda.")
            st.info(
                f"**Análise Financeira:**\n"
                f"- Comprometimento solicitado: **{percentual:.1f}%** da renda.\n"
                f"- Parcela máxima permitida (30%): **R$ {parcela_maxima:,.2f}**\n\n"
                f"💡 **Sugestão:** Para ser aprovado, ajuste a parcela para até **R$ {parcela_maxima:,.2f}** "
                f"aumentando o número de parcelas ou dando uma entrada maior."
            )
        else:
            st.success("🎉 Crédito APROVADO! Sua parcela está dentro do limite de segurança financeiro.")
            st.metric("Comprometimento da Renda", f"{percentual:.1f}%", "Dentro do limite (máx. 30%)")