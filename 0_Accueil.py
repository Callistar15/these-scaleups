import streamlit as st
import pandas as pd
import numpy as np

# --- Titre principal ---
st.title("📊 Dashboard de test - Scale-ups européennes")

# --- Introduction ---
st.write("Exemple de visualisation avec **données fictives** (Fake Data).")

# --- Section 1 : Indicateurs clés ---
st.header("🌍 KPIs principaux")
col1, col2, col3 = st.columns(3)
col1.metric("Deals M&A", "125", "+12%")
col2.metric("Levées de fonds", "€8.4B", "-5%")
col3.metric("Scale-ups IA", "42", "+7")

# --- Section 2 : Tableau de données fictives ---
st.header("📈 Échantillon de deals (fictif)")
fake_data = {
    "Société": ["DeepFake AI", "ClimateX", "NeoBankX", "GreenEnergy", "DataBoost"],
    "Secteur": ["IA", "Climate Tech", "FinTech", "Climate Tech", "AdTech"],
    "Valorisation (€M)": [850, 1200, 670, 540, 310],
    "Année": [2024, 2025, 2025, 2024, 2025]
}
df = pd.DataFrame(fake_data)
st.dataframe(df)

# --- Section 3 : Graphique ---
st.header("📊 Evolution du financement (fictif)")
years = np.arange(2019, 2026)
funding = np.random.randint(200, 1200, size=len(years))
chart_data = pd.DataFrame({"Année": years, "Montant (€M)": funding})
st.line_chart(chart_data.set_index("Année"))

# --- Section 4 : Interactivité ---
st.header("⚙️ Simulation")
value = st.slider("Choisis un multiple EV/EBITDA (fictif)", 5, 25, 12)
st.write(f"➡️ Avec un multiple de {value}x, une EBITDA de €10M donnerait une valo de **€{value*10}M**")
