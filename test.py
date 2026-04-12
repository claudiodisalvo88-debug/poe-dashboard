import os
import csv
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="PoE Dashboard", layout="wide")

# =========================
# CONFIG
# =========================
APP_TITLE = "⚡ Proof of Energy (PoE)"
APP_SUBTITLE = "Sistema di monitoraggio energetico con Energy Reputation dei nodi"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "poe_data.csv")

REQUIRED_COLUMNS = ["timestamp", "node_id", "energy_wh", "watt"]
ONLINE_THRESHOLD_SECONDS = 15


# =========================
# UTILS
# =========================
def detect_separator(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        sample = f.read(2048)
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=";,")
        return dialect.delimiter
    except Exception:
        return ";"


@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError("File poe_data.csv non trovato nella stessa cartella di test.py")

    sep = detect_separator(file_path)
    df = pd.read_csv(file_path, sep=sep)

    df.columns = df.columns.str.strip().str.lower()

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Colonne mancanti nel CSV: {missing}. Colonne trovate: {list(df.columns)}")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["energy_wh"] = pd.to_numeric(df["energy_wh"], errors="coerce")
    df["watt"] = pd.to_numeric(df["watt"], errors="coerce")
    df["node_id"] = df["node_id"].astype(str).str.strip()

    df = df.dropna(subset=["timestamp", "energy_wh", "watt", "node_id"]).copy()
    df = df.sort_values("timestamp")

    if df.empty:
        raise ValueError("Il CSV è stato letto, ma dopo la pulizia non sono rimasti dati validi.")

    return df


def apply_time_filter(df: pd.DataFrame, option: str) -> pd.DataFrame:
    latest_ts = df["timestamp"].max()

    if option == "Tutti":
        return df
    if option == "Ultimi 5 minuti":
        return df[df["timestamp"] >= latest_ts - pd.Timedelta(minutes=5)]
    if option == "Ultima ora":
        return df[df["timestamp"] >= latest_ts - pd.Timedelta(hours=1)]
    if option == "Ultime 24 ore":
        return df[df["timestamp"] >= latest_ts - pd.Timedelta(hours=24)]

    return df


def calculate_reputation(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for node_id, group in df.groupby("node_id"):
        total_energy = float(group["energy_wh"].sum())
        stability = float(group["watt"].std()) if len(group) > 1 else 0.0

        if pd.isna(stability):
            stability = 0.0

        reputation = total_energy / (1 + stability)

        if stability <= 10:
            quality = "stable"
        elif stability <= 25:
            quality = "warning"
        else:
            quality = "critical"

        last_seen = group["timestamp"].max()
        seconds_from_last = (pd.Timestamp.now() - last_seen).total_seconds()
        connection_status = "online" if seconds_from_last <= ONLINE_THRESHOLD_SECONDS else "offline"

        rows.append(
            {
                "node_id": node_id,
                "total_energy": round(total_energy, 2),
                "stability": round(stability, 2),
                "reputation": round(reputation, 2),
                "quality": quality,
                "last_seen": last_seen,
                "connection_status": connection_status,
            }
        )

    rep_df = pd.DataFrame(rows)

    if rep_df.empty:
        return rep_df

    return rep_df.sort_values(by="reputation", ascending=False).reset_index(drop=True)


def build_time_chart(df: pd.DataFrame) -> pd.DataFrame:
    chart_df = (
        df.groupby("timestamp", as_index=False)["watt"]
        .mean()
        .sort_values("timestamp")
        .set_index("timestamp")
    )
    return chart_df


def evaluate_network_quality(rep_df: pd.DataFrame) -> str:
    if rep_df.empty:
        return "unknown"

    critical_count = (rep_df["quality"] == "critical").sum()
    warning_count = (rep_df["quality"] == "warning").sum()

    if critical_count > 0:
        return "critical"
    if warning_count > 0:
        return "warning"
    return "stable"


# =========================
# SIDEBAR CONTROLS
# =========================
st.sidebar.title("Controlli")

time_filter = st.sidebar.selectbox(
    "Intervallo dati",
    ["Tutti", "Ultimi 5 minuti", "Ultima ora", "Ultime 24 ore"],
    index=0,
)

auto_refresh = st.sidebar.checkbox("🔄 Auto refresh live", value=True)

refresh_seconds = st.sidebar.selectbox(
    "Frequenza refresh",
    [5, 10, 15, 30],
    index=0,
)

manual_refresh = st.sidebar.button("🔄 Ricarica dati ora")

if manual_refresh:
    st.cache_data.clear()
    st.rerun()

if auto_refresh:
    st_autorefresh(interval=refresh_seconds * 1000, key="poe_live_refresh")
    st.cache_data.clear()


# =========================
# UI
# =========================
st.title(APP_TITLE)
st.markdown(APP_SUBTITLE)

try:
    raw_df = load_data(FILE_PATH)
except Exception as e:
    st.error(str(e))
    st.stop()

latest_update = raw_df["timestamp"].max()

st.markdown("---")
st.subheader("📊 Executive Summary")

colA, colB, colC = st.columns(3)

colA.metric(
    "Energia totale rete",
    f"{raw_df['energy_wh'].sum():.0f} Wh"
)

colB.metric(
    "Numero nodi monitorati",
    int(raw_df["node_id"].nunique())
)

colC.metric(
    "Ultimo aggiornamento",
    latest_update.strftime("%H:%M:%S")
)

st.markdown(
    """
Questo sistema dimostra un primo prototipo di **Proof of Energy (PoE)**:
- raccolta dati energetici distribuiti
- analisi stabilità nodi
- generazione reputazione energetica
- monitoraggio stato rete in tempo reale
"""
)

df = apply_time_filter(raw_df, time_filter)

if df.empty:
    st.warning("Nessun dato disponibile con il filtro selezionato.")
    st.stop()

rep_df = calculate_reputation(df)
time_chart = build_time_chart(df)

online_nodes = int((rep_df["connection_status"] == "online").sum()) if not rep_df.empty else 0
offline_nodes = int((rep_df["connection_status"] == "offline").sum()) if not rep_df.empty else 0
network_quality = evaluate_network_quality(rep_df)

# KPI
col1, col2, col3, col4 = st.columns(4)
col1.metric("⚡ Energia Totale (Wh)", f"{df['energy_wh'].sum():.2f}")
col2.metric("🔌 Potenza Media (W)", f"{df['watt'].mean():.2f}")
col3.metric("🟢 Nodi Online", online_nodes)
col4.metric("🔴 Nodi Offline", offline_nodes)

st.divider()

col5, col6 = st.columns(2)
col5.metric("🧠 Nodi Attivi", int(df["node_id"].nunique()))
col6.metric("⏱ Ultimo Update", latest_update.strftime("%H:%M:%S"))

if network_quality == "stable":
    st.success("🟢 Qualità rete: STABILE")
elif network_quality == "warning":
    st.warning("🟡 Qualità rete: ATTENZIONE")
else:
    st.error("🔴 Qualità rete: CRITICA")

st.divider()

# Charts
st.subheader("📈 Andamento Potenza Media nel Tempo")
st.line_chart(time_chart, height=320)

st.subheader("🏆 Energy Reputation per Nodo")
if not rep_df.empty:
    rep_chart = rep_df.set_index("node_id")[["reputation"]]
    st.bar_chart(rep_chart, height=320)
else:
    st.warning("Nessun dato reputazione disponibile.")

st.divider()

# Top node + table
left, right = st.columns([1, 2])

with left:
    st.subheader("🥇 Top Node")

    if not rep_df.empty:
        top_node = rep_df.iloc[0]

        st.success(
            f"Nodo: {top_node['node_id']}\n\n"
            f"Reputation: {top_node['reputation']}\n\n"
            f"Energia: {top_node['total_energy']} Wh\n\n"
            f"Stabilità: {top_node['stability']}\n\n"
            f"Qualità: {top_node['quality']}\n\n"
            f"Stato: {top_node['connection_status']}"
        )
    else:
        st.warning("Nessun nodo disponibile.")

with right:
    st.subheader("📋 Stato Completo Nodi")

    if not rep_df.empty:
        display_df = rep_df.copy()
        display_df["last_seen"] = display_df["last_seen"].dt.strftime("%Y-%m-%d %H:%M:%S")
        st.dataframe(
            display_df,
            width="stretch",
            hide_index=True
        )
    else:
        st.warning("Nessun ranking disponibile.")

st.divider()

st.subheader("ℹ️ Come funziona PoE")
st.markdown(
    """
PoE raccoglie dati energetici dai nodi e misura:

- energia prodotta
- stabilità del segnale
- reputazione energetica
- stato online/offline dei nodi

L'obiettivo è valutare quali nodi sono più affidabili nella rete.
"""
)
