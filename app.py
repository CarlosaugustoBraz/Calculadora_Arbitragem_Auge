import streamlit as st

def calcular_arbitragem(preco_venda, preco_compra, custo_transacao):
    return (preco_venda - preco_compra) - custo_transacao

def calcular_juros_ponderados(capitais, taxas, tempos):
    total_ponderado = sum(c * t * p for c, t, p in zip(capitais, taxas, tempos))
    total_capital = sum(capitais)
    return total_ponderado / total_capital

st.title("📊 Calculadora de Arbitragem e Juros Ponderados")

# Seção de Arbitragem
st.header("💰 Cálculo de Arbitragem")
preco_compra = st.number_input("Preço de Compra", min_value=0.0, step=0.01)
preco_venda = st.number_input("Preço de Venda", min_value=0.0, step=0.01)
custo_transacao = st.number_input("Custo da Transação", min_value=0.0, step=0.01)

if st.button("Calcular Arbitragem"):
    lucro = calcular_arbitragem(preco_venda, preco_compra, custo_transacao)
    st.success(f"Lucro da Arbitragem: R$ {lucro:.2f}")

# Seção de Juros Ponderados
st.header("📈 Cálculo de Juros Ponderados")
num_investimentos = st.number_input("Número de Investimentos", min_value=1, step=1)

capitais = []
taxas = []
tempos = []

for i in range(num_investimentos):
    st.subheader(f"Investimento {i+1}")
    capitais.append(st.number_input(f"Capital Investido {i+1}", min_value=0.0, step=0.01))
    taxas.append(st.number_input(f"Taxa de Juros {i+1} (%)", min_value=0.0, step=0.01))
    tempos.append(st.number_input(f"Tempo {i+1} (meses)", min_value=1, step=1))

if st.button("Calcular Juros Ponderados"):
    if sum(capitais) > 0:
        juros_medio = calcular_juros_ponderados(capitais, taxas, tempos)
        st.success(f"Juros Ponderados: {juros_medio:.2f}% ao mês")
    else:
        st.error("O capital investido deve ser maior que zero.")
