import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# =========================
# CONFIG
# =========================
API_BASE_URL = "http://127.0.0.1:8000"
APP_TITLE = "Proof of Energy"
APP_SUBTITLE = "Sistema di monitoraggio e confronto dell'affidabilità energetica dei nodi"

st.set_page_config(
    page_title="PoE Dashboard",
    page_icon="⚡",
    layout="wide",
)

# =========================
# STYLE
# =========================
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }

        .title-main {
            font-size: 2.3rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 0.15rem;
            letter-spacing: -0.03em;
        }

        .title-sub {
            font-size: 1rem;
            color: #6b7280;
            margin-bottom: 1.2rem;
        }

        .hero {
            background: linear-gradient(135deg, #0f172a 0%, #111827 60%, #1f2937 100%);
            border-radius: 22px;
            padding: 1.4rem 1.5rem;
            color: white;
            border: 1px solid rgba(255,255,255,0.08);
            margin-bottom: 1.1rem;
        }

        .hero-title {
            font-size: 1.25rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
        }

        .hero-text {
            color: #d1d5db;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            padding: 1rem 1rem 0.9rem 1rem;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
        }

        .label {
            font-size: 0.82rem;
            color: #6b7280;
            margin-bottom: 0.3rem;
        }

        .value {
            font-size: 1.7rem;
            font-weight: 800;
            color: #111827;
            line-height: 1.1;
        }

        .note {
            margin-top: 0.3rem;
            color: #6b7280;
            font-size: 0.8rem;
        }

        .section-title {
            font-size: 1.08rem;
            font-weight: 700;
            margin-top: 0.25rem;
            margin-bottom: 0.55rem;
            color: #111827;
        }

        .panel {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            padding: 1rem;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
        }

        .mini-label {
            color: #6b7280;
            font-size: 0.8rem;
            margin-bottom: 0.15rem;
        }

        .mini-value {
            color: #111827;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.65rem;
        }

        .badge {
            display: inline-block;
            padding: 0.35rem 0.72rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 800;
        }

        .stable {
            background: rgba(16, 185, 129, 0.12);
            color: #047857;
        }

        .warning {
            background: rgba(245, 158, 11, 0.15);
            color: #b45309;
        }

        .critical {
            background: rgba(239, 68, 68, 0.12);
            color: #b91c1c;
        }

        .neutral {
            background: rgba(107, 114, 128, 0.12);
            color: #374151;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# HELPERS
# =========================
def get_badge(label: str, status: str) -> str:
    status = (status or "").lower()

    if status in ["ok", "healthy", "stable"]:
        cls = "stable"
    elif status in ["warning", "attenzione"]:
        cls = "warning"
    elif status in ["critical", "critica", "error"]:
        cls = "critical"
    else:
        cls = "neutral"

    return f'<span class="badge {cls}">{label}</span>'


@st.cache_data(ttl=5)
def fetch_json(url: str):
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()


def load_data():
    health = fetch_json(f"{API_BASE_URL}/health")
    nodes = fetch_json(f"{API_BASE_URL}/nodes")
    summary = fetch_json(f"{API_BASE_URL}/summary")
    reputation = fetch_json(f"{API_BASE_URL}/reputation")
    return health, nodes, summary, reputation


# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.header("Controlli")
    auto_refresh = st.checkbox("Auto refresh", value=True)
    refresh_seconds = st.selectbox("Intervallo refresh", [5, 10, 15, 30], index=0)
    manual_refresh = st.button("Ricarica ora")
    st.caption("La dashboard legge direttamente il backend PoE.")

if manual_refresh:
    st.cache_data.clear()
    st.rerun()

if auto_refresh:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=refresh_seconds * 1000, key="poe_refresh")
    st.cache_data.clear()

# =========================
# LOAD
# =========================
st.markdown(f'<div class="title-main">⚡ {APP_TITLE}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="title-sub">{APP_SUBTITLE}</div>', unsafe_allow_html=True)

try:
    health_data, nodes_data, summary_data, reputation_data = load_data()
except Exception as e:
    st.error(f"Errore connessione API: {e}")
    st.stop()

nodes_df = pd.DataFrame(nodes_data)
reputation_df = pd.DataFrame(reputation_data)

# =========================
# HERO
# =========================
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">Sistema attivo</div>
        <div class="hero-text">
            PoE non si limita a mostrare dati energetici. 
            Misura la continuità del flusso, rende confrontabili i nodi
            e costruisce una prima lettura dell'affidabilità energetica.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# KPI ROW
# =========================
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        f"""
        <div class="card">
            <div class="label">Energia totale</div>
            <div class="value">{summary_data.get('total_energy', 0):.2f} Wh</div>
            <div class="note">Energia aggregata osservata</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k2:
    st.markdown(
        f"""
        <div class="card">
            <div class="label">Potenza media</div>
            <div class="value">{summary_data.get('avg_power', 0):.2f} W</div>
            <div class="note">Media dei watt registrati</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k3:
    st.markdown(
        f"""
        <div class="card">
            <div class="label">Nodi unici</div>
            <div class="value">{summary_data.get('nodes', 0)}</div>
            <div class="note">Nodi rilevati dal backend</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k4:
    st.markdown(
        f"""
        <div class="card">
            <div class="label">Record raccolti</div>
            <div class="value">{summary_data.get('records', 0)}</div>
            <div class="note">Numero totale osservazioni</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

# =========================
# STATUS + SUMMARY
# =========================
left, right = st.columns([1.1, 1.9])

with left:
    st.markdown('<div class="section-title">Stato sistema</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown('<div class="mini-label">Backend</div>', unsafe_allow_html=True)
    st.markdown(get_badge(health_data.get("status", "unknown").upper(), health_data.get("status", "unknown")), unsafe_allow_html=True)

    st.markdown('<div class="mini-label" style="margin-top:0.9rem;">Servizio</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mini-value">{health_data.get("service", "n/a")}</div>', unsafe_allow_html=True)

    if not reputation_df.empty:
        top_node = reputation_df.iloc[0]

        st.markdown('<div class="mini-label">Nodo top ranking</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mini-value">{top_node["node_id"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="mini-label">Reputation</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mini-value">{top_node["reputation"]}</div>', unsafe_allow_html=True)

        stability_val = float(top_node["stability"])
        if stability_val <= 10:
            q = "stable"
        elif stability_val <= 25:
            q = "warning"
        else:
            q = "critical"

        st.markdown('<div class="mini-label">Qualità nodo</div>', unsafe_allow_html=True)
        st.markdown(get_badge(q.upper(), q), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-title">Executive summary</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="panel">
            <div class="mini-label">Che cosa stai guardando</div>
            <div class="mini-value">Un sistema che confronta l'affidabilità energetica dei nodi su dati raccolti dal backend.</div>

            <div class="mini-label">Che cosa è già utile</div>
            <div class="mini-value">Monitoraggio, riepilogo energetico, lettura del ranking e confronto tra nodi.</div>

            <div class="mini-label">Che cosa conta davvero</div>
            <div class="mini-value">Stabilità del sistema, continuità del dato e differenze leggibili tra nodi reali o simulati.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs(["Trend dati", "Ranking", "Dati grezzi"])

with tab1:
    st.markdown('<div class="section-title">Andamento potenza nel tempo</div>', unsafe_allow_html=True)

    if not nodes_df.empty and "timestamp" in nodes_df.columns:
        plot_df = nodes_df.copy()
        plot_df["timestamp"] = pd.to_datetime(plot_df["timestamp"], errors="coerce")
        plot_df = plot_df.dropna(subset=["timestamp"])

        if not plot_df.empty:
            trend = (
                plot_df.groupby("timestamp", as_index=False)["watt"]
                .mean()
                .sort_values("timestamp")
                .set_index("timestamp")
            )
            st.line_chart(trend, height=340)
        else:
            st.info("Nessun dato valido disponibile per il grafico.")
    else:
        st.info("Nessun dato disponibile.")

with tab2:
    st.markdown('<div class="section-title">Ranking nodi</div>', unsafe_allow_html=True)

    if not reputation_df.empty:
        chart_df = reputation_df.set_index("node_id")[["reputation"]]
        st.bar_chart(chart_df, height=320)

        st.markdown('<div class="section-title">Tabella reputazione</div>', unsafe_allow_html=True)
        st.dataframe(reputation_df, width="stretch", hide_index=True)
    else:
        st.info("Nessun ranking disponibile.")

with tab3:
    st.markdown('<div class="section-title">Dati grezzi ricevuti</div>', unsafe_allow_html=True)

    if not nodes_df.empty:
        st.dataframe(nodes_df, width="stretch", hide_index=True)
    else:
        st.info("Nessun dato nodo disponibile.")