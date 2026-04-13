import streamlit as st
import pandas as pd
import requests
from requests.exceptions import RequestException
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="PoE Dashboard", layout="wide")

API_URL = "http://127.0.0.1:8000"
st_autorefresh(interval=5000, key="refresh")

def fetch_json(endpoint: str):
    url = f"{API_URL}{endpoint}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

try:
    nodes = fetch_json("/nodes")
    summary = fetch_json("/summary")
    rep = fetch_json("/reputation")
except RequestException:
    st.error("API non raggiungibile. Avvia prima `python -m uvicorn api:app --reload`.")
    st.stop()

df = pd.DataFrame(nodes)
rep_df = pd.DataFrame(rep)

if df.empty or rep_df.empty:
    st.warning("Nessun dato disponibile dall'API.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"]).sort_values("timestamp")

st.title("⚡ Proof of Energy (PoE)")
st.markdown("Sistema di monitoraggio energetico con Energy Reputation dei nodi")
st.markdown("🚀 Sistema attivo — dati via API")
st.markdown("---")

st.subheader("📊 Executive Summary")
c1, c2, c3 = st.columns(3)
c1.metric("⚡ Energia Totale", f"{summary['total_energy']:.2f}")
c2.metric("🔌 Potenza Media", f"{summary['avg_power']:.2f}")
c3.metric("🧠 Nodi", summary["nodes"])

st.markdown("---")

k1, k2, k3 = st.columns(3)
k1.metric("📊 Records", summary["records"])
k2.metric("📡 Ultimo update", df["timestamp"].max().strftime("%H:%M:%S"))
k3.metric("🏆 Top Node", rep_df.iloc[0]["node_id"])

st.subheader("📈 Potenza nel Tempo")
chart = df.groupby("timestamp")["watt"].mean().sort_index()
st.line_chart(chart)

st.subheader("🏆 Energy Reputation")
st.bar_chart(rep_df.set_index("node_id")["reputation"])

st.subheader("📋 Dati")
st.dataframe(df.tail(50), width="stretch", hide_index=True)

st.subheader("🥇 Top Node")
top = rep_df.iloc[0]
st.success(
    f"Nodo: {top['node_id']}\n\n"
    f"Reputation: {top['reputation']}\n\n"
    f"Energia: {top['energy']}\n\n"
    f"Stabilità: {top['stability']}"
)
