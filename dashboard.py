import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="PoE Dashboard", layout="wide")

# HEADER
st.title("⚡ Proof of Energy (PoE)")
st.markdown("Monitoraggio energetico in tempo reale + Energy Reputation")

# PATH SICURO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "poe_data.csv")

# --- FUNZIONE ENERGY REPUTATION ---
def calculate_reputation(df):
    grouped = df.groupby("node_id")

    reputation_data = []

    for node, data in grouped:
        total_energy = data["energy_wh"].sum()
        stability = data["watt"].std() if len(data) > 1 else 0

        # Formula semplice MVP:
        # più energia = meglio
        # meno variazione = meglio
        score = total_energy / (1 + stability)

        reputation_data.append({
            "node_id": node,
            "reputation": round(score, 2)
        })

    return pd.DataFrame(reputation_data).sort_values("reputation", ascending=False)

# --- LOOP LIVE ---
placeholder = st.empty()

while True:
    with placeholder.container():

        # CONTROLLO FILE
        if not os.path.exists(FILE_PATH):
            st.error("File dati non trovato")
            st.info("Avvia test.py prima")
            st.stop()

        try:
            df = pd.read_csv(FILE_PATH, sep=";")
        except Exception as e:
            st.error(f"Errore lettura file: {e}")
            st.stop()

        if df.empty:
            st.warning("Nessun dato disponibile")
            st.stop()

        # PARSING
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])

        # KPI
        total_energy = df["energy_wh"].sum()
        avg_power = df["watt"].mean()
        nodes = df["node_id"].nunique()

        st.subheader("📊 KPI Principali")

        col1, col2, col3 = st.columns(3)
        col1.metric("Energia Totale (Wh)", round(total_energy, 2))
        col2.metric("Potenza Media (W)", round(avg_power, 2))
        col3.metric("Nodi Attivi", nodes)

        st.divider()

        # ENERGY REPUTATION
        st.subheader("🏆 Energy Reputation")

        rep_df = calculate_reputation(df)

        st.dataframe(rep_df, use_container_width=True)

        st.bar_chart(rep_df.set_index("node_id")["reputation"])

        st.divider()

        # ANALISI
        st.subheader("⚡ Analisi Energetica")

        colA, colB = st.columns(2)

        with colA:
            st.markdown("**Energia per nodo**")
            st.bar_chart(df.groupby("node_id")["energy_wh"].sum())

        with colB:
            st.markdown("**Stato nodi**")
            st.bar_chart(df["state"].value_counts())

        st.divider()

        # TIME SERIES
        st.subheader("📈 Andamento nel tempo")

        df = df.sort_values("timestamp")
        st.line_chart(df.set_index("timestamp")["watt"])

        st.divider()

        # DATI
        st.subheader("📄 Dati grezzi")
        st.dataframe(df, use_container_width=True)

    time.sleep(3)