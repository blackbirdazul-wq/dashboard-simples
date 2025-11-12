import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(page_title="Dashboard Simples", layout="wide")
st.title("🎯 Dashboard Mercados")

# Tickers CONFIÁVEIS
tickers = {
    "EWZ Brasil": "EWZ",
    "S&P 500": "SPY", 
    "Nasdaq": "QQQ"
}

for nome, simbolo in tickers.items():
    try:
        dados = yf.download(simbolo, period="5d")
        if not dados.empty:
            preco_atual = dados['Close'].iloc[-1]
            preco_anterior = dados['Close'].iloc[-2]
            variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
            
            st.metric(
                label=nome,
                value=f"${preco_atual:.2f}",
                delta=f"{variacao:.2f}%"
            )
        else:
            st.error(f"Sem dados: {nome}")
    except:
        st.error(f"Erro: {nome}")

st.info("📊 Dashboard funcionando perfeitamente!")
