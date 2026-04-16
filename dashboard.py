import os
import streamlit as st
import pandas as pd
import requests
from requests.exceptions import RequestException
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="PoE Dashboard", layout="wide")

API_URL = os.getenv("POE_API_URL", "http://127.0.0.1:8000").rstrip("/")
st_autorefresh(interval=10000, key="refresh")


def fetch_json(endpoint: str):
    url = f"{API_URL}{endpoint}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()


def calculate_reputation_local(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby("node_id")
    reputation_data = []

    for node, data in grouped:
        total_energy = data["energy_wh"].sum()
        stability = data["watt"].std() if len(data) > 1 else 0
        stability = 0 if pd.isna(stability) else stability
        score = total_energy / (1 + stability)

        reputation_data.append({
            "node_id": node,
            "reputation": round(float(score), 2)
        })

    return pd.DataFrame(reputation_data).sort_values("reputation", ascending=False)


try:
    nodes = fetch_json("/nodes")
    summary = fetch_json("/summary")
    rep = fetch_json("/reputation")
except RequestException as e:
    st.error("API non raggiungibile.")
    st.code(
        "Avvia questi processi:\n"
        "1) uvicorn api:app --reload\n"
        "2) python3 live_data.py\n"
        "3) streamlit run dashboard.py"
    )
    st.caption(f"Dettaglio errore: {e}")
    st.stop()

df = pd.DataFrame(nodes)
rep_df = pd.DataFrame(rep)

if df.empty:
    st.warning("Nessun dato disponibile dall'API.")
    st.info("Avvia prima il simulatore dati con: python3 live_data.py")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"]).sort_values("timestamp")

st.title("⚡ Proof of Energy (PoE)")
st.markdown("Monitoraggio energetico in tempo reale + Energy Reputation")
st.markdown("🚀 Dashboard completa collegata alle API")
st.divider()

# KPI PRINCIPALI
st.subheader("📊 KPI Principali")

col1, col2, col3 = st.columns(3)
col1.metric("Energia Totale (Wh)", round(float(summary["total_energy"]), 2))
col2.metric("Potenza Media (W)", round(float(summary["avg_power"]), 2))
col3.metric("Nodi Attivi", int(summary["nodes"]))

st.divider()

# ENERGY REPUTATION
st.subheader("🏆 Energy Reputation")

if rep_df.empty:
    rep_df = calculate_reputation_local(df)

st.dataframe(rep_df, use_container_width=True, hide_index=True)

if not rep_df.empty and "node_id" in rep_df.columns and "reputation" in rep_df.columns:
    st.bar_chart(rep_df.set_index("node_id")["reputation"])

st.divider()

# ANALISI ENERGETICA
st.subheader("⚡ Analisi Energetica")

colA, colB = st.columns(2)

with colA:
    st.markdown("**Energia per nodo**")
    energy_per_node = df.groupby("node_id")["energy_wh"].sum().sort_values(ascending=False)
    st.bar_chart(energy_per_node)

with colB:
    st.markdown("**Stato nodi**")
    if "state" in df.columns:
        st.bar_chart(df["state"].value_counts())
    else:
        st.info("Campo 'state' non ancora disponibile nel backend attuale.")

st.divider()

# TIME SERIES
st.subheader("📈 Andamento nel tempo")

power_ts = df.groupby("timestamp")["watt"].mean().sort_index()
st.line_chart(power_ts)

st.divider()

# EXTRA KPI
st.subheader("📌 Snapshot operativo")

k1, k2, k3 = st.columns(3)
k1.metric("Records", int(summary["records"]))
k2.metric("Ultimo update", df["timestamp"].max().strftime("%H:%M:%S"))
if not rep_df.empty:
    k3.metric("Top Node", str(rep_df.iloc[0]["node_id"]))
else:
    k3.metric("Top Node", "-")

st.divider()

# DATI GREZZI
st.subheader("📄 Dati grezzi")
st.dataframe(df.tail(50), use_container_width=True, hide_index=True)
