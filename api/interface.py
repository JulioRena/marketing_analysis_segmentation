import streamlit as st
import requests


api_url = "http://localhost:8000/predict"

st.title("Previsão de Categoria")
st.write("Insira os valores das variáveis para prever a categoria.")

income = st.number_input("Income", min_value=0.0, step=0.1)
spending_score = st.number_input("Spending Score", min_value=0.0, step=0.1)
membership_years = st.number_input("Membership Years", min_value=0.0, step=0.1)
purchase_frequency = st.number_input("Purchase Frequency", min_value=0.0, step=0.1)
last_purchase_amount = st.number_input("Last Purchase Amount", min_value=0.0, step=0.1)

if st.button("Prever"):
    data = {
        "income": income,
        "spending_score": spending_score,
        "membership_years": membership_years,
        "purchase_frequency": purchase_frequency,
        "last_purchase_amount": last_purchase_amount
    }

    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result = response.json()
        st.write(f"Este cliente se encaixa no Cluster: {result['Cluster']}")
    else:
        st.write("Ocorreu um erro ao fazer a previsão. Por favor, tente novamente.")

