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
        # Método MAIS CONFIÁVEL
        ticker = yf.Ticker(simbolo)
        dados = ticker.history(period="5d")
        
        if not dados.empty and len(dados) > 1:
            preco_atual = dados['Close'].iloc[-1]
            preco_anterior = dados['Close'].iloc[-2]
            variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
            
            st.metric(
                label=f"{nome} ({simbolo})",
                value=f"${preco_atual:.2f}",
                delta=f"{variacao:.2f}%"
            )
        else:
            st.error(f"Sem dados suficientes: {nome}")
            
    except Exception as e:
        st.error(f"Erro em {nome}: {str(e)}")

st.success("✅ Dashboard carregado com sucesso!")
