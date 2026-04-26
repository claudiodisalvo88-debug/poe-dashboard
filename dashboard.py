import os
import pandas as pd
import requests
import streamlit as st
from requests.exceptions import RequestException

st.set_page_config(
    page_title="Proof of Energy",
    page_icon="⚡",
    layout="wide",
)

API_URL = os.getenv("POE_API_URL", "http://127.0.0.1:8000").rstrip("/")


@st.cache_data(ttl=20)
def fetch_json(endpoint: str):
    response = requests.get(f"{API_URL}{endpoint}", timeout=5)
    response.raise_for_status()
    return response.json()


def calculate_reputation_local(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for node_id, group in df.groupby("node_id"):
        total_energy = float(group["energy_wh"].sum())
        stability = float(group["watt"].std()) if len(group) > 1 else 0.0
        if pd.isna(stability):
            stability = 0.0

        reputation = total_energy / (1 + stability)

        rows.append(
            {
                "Node": node_id,
                "Reputation": round(reputation, 2),
                "Energy Wh": round(total_energy, 2),
                "Stability": round(stability, 2),
            }
        )

    return pd.DataFrame(rows).sort_values("Reputation", ascending=False)


def classify_quality(rep_df: pd.DataFrame) -> str:
    if rep_df.empty or "Stability" not in rep_df.columns:
        return "N/D"

    worst = float(rep_df["Stability"].max())
    if worst <= 10:
        return "Stabile"
    if worst <= 25:
        return "Attenzione"
    return "Critica"


st.markdown(
    """
    <style>
        .block-container {
            max-width: 1280px;
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        h1, h2, h3 {
            letter-spacing: -0.02em;
        }

        .hero {
            background: linear-gradient(135deg, #0f172a 0%, #111827 65%, #1e293b 100%);
            border-radius: 18px;
            padding: 1.25rem 1.35rem;
            margin-bottom: 1rem;
            color: white;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .hero-title {
            font-size: 1.2rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
        }

        .hero-text {
            font-size: 0.94rem;
            line-height: 1.5;
            color: #dbe4ee;
        }

        .mini-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 0.9rem 1rem;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
        }

        .mini-label {
            color: #64748b;
            font-size: 0.78rem;
            margin-bottom: 0.2rem;
        }

        .mini-value {
            color: #0f172a;
            font-size: 1.55rem;
            font-weight: 800;
            line-height: 1.05;
        }

        .mini-note {
            color: #64748b;
            font-size: 0.78rem;
            margin-top: 0.25rem;
        }

        .status-box {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
            height: 100%;
        }

        .status-pill {
            display: inline-block;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 800;
            margin-top: 0.2rem;
            margin-bottom: 0.6rem;
        }

        .stable {
            background: rgba(16, 185, 129, 0.12);
            color: #047857;
        }

        .warning {
            background: rgba(245, 158, 11, 0.14);
            color: #b45309;
        }

        .critical {
            background: rgba(239, 68, 68, 0.12);
            color: #b91c1c;
        }

        .neutral {
            background: rgba(100, 116, 139, 0.12);
            color: #334155;
        }

        .insight-box {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
            height: 100%;
        }

        .insight-item {
            padding: 0.7rem 0;
            border-bottom: 1px solid #eef2f7;
        }

        .insight-item:last-child {
            border-bottom: none;
        }

        .insight-label {
            color: #64748b;
            font-size: 0.78rem;
            margin-bottom: 0.2rem;
        }

        .insight-value {
            color: #0f172a;
            font-size: 0.95rem;
            font-weight: 700;
            line-height: 1.4;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Controlli")
    auto_refresh = st.checkbox("Auto refresh", value=False)
    refresh_seconds = st.selectbox("Intervallo refresh", [15, 30, 60], index=1)
    if st.button("Ricarica dati"):
        st.cache_data.clear()
        st.rerun()

if auto_refresh:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=refresh_seconds * 1000, key="poe_refresh")

try:
    health = fetch_json("/health")
    nodes = fetch_json("/nodes")
    reputation = fetch_json("/reputation")
except RequestException as e:
    st.error("API non raggiungibile.")
    st.code(
        "Avvia questi processi:\n"
        "1) python3 -m uvicorn api:app --reload\n"
        "2) python3 multi_node_sender.py\n"
        "3) streamlit run dashboard.py"
    )
    st.caption(f"Dettaglio errore: {e}")
    st.stop()

df = pd.DataFrame(nodes)
rep_df = pd.DataFrame(reputation)

if df.empty:
    st.warning("Nessun dato disponibile dall'API.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"]).sort_values("timestamp")

if rep_df.empty:
    rep_df = calculate_reputation_local(df)
else:
    rep_df = rep_df.rename(
        columns={
            "node_id": "Node",
            "reputation": "Reputation",
            "energy": "Energy Wh",
            "stability": "Stability",
        }
    )

total_energy = round(float(df["energy_wh"].sum()), 2)
avg_power = round(float(df["watt"].mean()), 2)
node_count = int(df["node_id"].nunique())
record_count = int(len(df))
last_update = df["timestamp"].max().strftime("%H:%M:%S")

network_quality = classify_quality(rep_df)
top_node = rep_df.iloc[0]["Node"] if not rep_df.empty else "-"
top_reputation = rep_df.iloc[0]["Reputation"] if not rep_df.empty else "-"

def pill_for(label: str):
    x = label.lower()
    if x in ["healthy", "ok", "stabile"]:
        cls = "stable"
    elif x in ["attenzione", "warning"]:
        cls = "warning"
    elif x in ["critica", "critical"]:
        cls = "critical"
    else:
        cls = "neutral"
    return f'<span class="status-pill {cls}">{label.upper()}</span>'

st.title("⚡ Proof of Energy")
st.caption("Sistema di monitoraggio e confronto dell’affidabilità energetica dei nodi")

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">MVP attivo</div>
        <div class="hero-text">
            PoE raccoglie dati energetici dai nodi, li confronta e costruisce una lettura iniziale
            dell’affidabilità energetica. Questa interfaccia serve a rendere il sistema leggibile,
            confrontabile e presentabile.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-label">Energia totale</div>
            <div class="mini-value">{total_energy}</div>
            <div class="mini-note">Wh aggregati nel dataset corrente</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-label">Potenza media</div>
            <div class="mini-value">{avg_power}</div>
            <div class="mini-note">Media dei watt osservati</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-label">Nodi attivi</div>
            <div class="mini-value">{node_count}</div>
            <div class="mini-note">Nodi distinti presenti nei dati</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-label">Ultimo update</div>
            <div class="mini-value">{last_update}</div>
            <div class="mini-note">Ultimo timestamp valido</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

left, right = st.columns([1, 2])

with left:
    st.markdown("#### Stato sistema")
    st.markdown('<div class="status-box">', unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Health backend</div>', unsafe_allow_html=True)
    st.markdown(pill_for(str(health.get("status", "N/D"))), unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Qualità rete</div>', unsafe_allow_html=True)
    st.markdown(pill_for(network_quality), unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Top node</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mini-value">{top_node}</div>', unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Top reputation</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mini-value">{top_reputation}</div>', unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Record raccolti</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mini-value">{record_count}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown("#### Lettura operativa")
    st.markdown(
        """
        <div class="insight-box">
            <div class="insight-item">
                <div class="insight-label">Che cosa stai guardando</div>
                <div class="insight-value">Un sistema che misura e rende confrontabile l’affidabilità energetica dei nodi.</div>
            </div>
            <div class="insight-item">
                <div class="insight-label">Che cosa è utile adesso</div>
                <div class="insight-value">Raccolta dati, riepilogo energetico, ranking nodi e lettura del comportamento della rete.</div>
            </div>
            <div class="insight-item">
                <div class="insight-label">Perché conta per il progetto</div>
                <div class="insight-value">Questo MVP mostra continuità del dato, confronto tra nodi e una base leggibile per il primo test reale.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

tab1, tab2, tab3 = st.tabs(["Trend rete", "Ranking nodi", "Dataset"])

with tab1:
    st.markdown("### Andamento potenza nel tempo")
    power_ts = df.groupby("timestamp", as_index=True)["watt"].mean().sort_index()
    st.line_chart(power_ts, height=300)

    st.markdown("### Energia per nodo")
    energy_per_node = df.groupby("node_id", as_index=True)["energy_wh"].sum().sort_values(ascending=False)
    st.bar_chart(energy_per_node, height=280)

with tab2:
    st.markdown("### Ranking nodi")
    if not rep_df.empty:
        st.bar_chart(rep_df.set_index("Node")[["Reputation"]], height=280)

    st.dataframe(rep_df, width="stretch", hide_index=True)

with tab3:
    st.markdown("### Dataset API")
    display_df = df.copy()
    display_df["timestamp"] = display_df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
    display_df = display_df.rename(
        columns={
            "timestamp": "Timestamp",
            "node_id": "Node",
            "watt": "Watt",
            "energy_wh": "Energy Wh",
        }
    )
    st.dataframe(display_df.tail(50), width="stretch", hide_index=True)