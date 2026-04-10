import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="PoE Dashboard", layout="wide")

st.title("⚡ Proof of Energy (PoE) Dashboard")

st.markdown("""
**PoE** è un sistema di valutazione energetica decentralizzato che assegna reputazione ai nodi in base a:

- produzione energetica
- stato operativo
- affidabilità complessiva

L'obiettivo è identificare i nodi più efficienti e affidabili, così da supportare un modello di accesso prioritario all’energia basato su performance reali.
""")

try:
    df = pd.read_csv("poe_data.csv", sep=";", header=None)
    df.columns = ["timestamp", "node_id", "volt", "ampere", "watt", "reputation", "state"]

    df["watt"] = pd.to_numeric(df["watt"], errors="coerce")
    df["reputation"] = pd.to_numeric(df["reputation"], errors="coerce")

    state_bonus = {
        "solar": 1.2,
        "battery": 1.0,
        "load": 0.8
    }

    df["state_multiplier"] = df["state"].map(state_bonus)
    df["energy_score"] = (df["watt"] * 0.7 + df["reputation"] * 0.3) * df["state_multiplier"]

    ranking = df.groupby("node_id")["energy_score"].mean().sort_values(ascending=False)
    best_node = ranking.index[0]
    best_score = ranking.iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("⚡ Energia media", round(df["watt"].mean(), 2))
    col2.metric("📊 Nodi attivi", df["node_id"].nunique())
    col3.metric("🏆 Best node", best_node)

    st.subheader("📄 Ultimi dati raccolti")
    st.write("Righe caricate:", len(df))
    st.dataframe(df.tail(10), use_container_width=True)

    st.subheader("⚡ Potenza media per nodo")
    st.bar_chart(df.groupby("node_id")["watt"].mean())

    st.subheader("🔋 Energy Reputation per nodo")
    st.bar_chart(df.groupby("node_id")["reputation"].mean())

    st.subheader("📈 Performance energetica nodi")
    st.bar_chart(df.groupby("node_id")["energy_score"].mean())

    st.subheader("🔌 Stato nodi")
    state_count = df["state"].value_counts()
    st.bar_chart(state_count)

    st.subheader("🧭 Legenda stati")
    st.markdown("""
- **solar** → nodo in produzione energetica  
- **battery** → nodo in accumulo / stabilizzazione  
- **load** → nodo in consumo energetico
""")

    st.subheader("🏆 Ranking nodi")
    st.dataframe(ranking, use_container_width=True)

    st.success(f"🔥 Nodo migliore: {best_node} (score: {round(best_score, 2)})")

    st.subheader("🧠 Insight del sistema")
    st.info(
        f"Il nodo con la migliore performance attuale è **{best_node}**, "
        f"con uno score medio di **{round(best_score, 2)}**. "
        f"Questo indica una combinazione più efficiente tra produzione, stato operativo e reputazione energetica."
    )

    time.sleep(2)
    st.rerun()

except FileNotFoundError:
    st.error("File poe_data.csv non trovato")

except pd.errors.EmptyDataError:
    st.warning("File vuoto. Avvia test.py")

except Exception as e:
    st.error(f"Errore: {e}")
    