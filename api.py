from fastapi import FastAPI
from db import read_data
import pandas as pd

app = FastAPI(
    title="Proof of Energy API",
    description="API del MVP Proof of Energy per monitoraggio nodi, summary energetico e ranking di Energy Reputation.",
    version="1.0.0"
)


def build_dataframe():
    data = read_data()

    df = pd.DataFrame(
        data,
        columns=[
            "timestamp",
            "node_id",
            "watt",
            "energy_wh"
        ]
    )

    if df.empty:
        return df

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    return df


@app.get("/", tags=["System"])
def home():
    return {
        "status": "ok",
        "service": "Proof of Energy API",
        "version": "1.0.0"
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy"
    }


@app.get("/nodes", tags=["Nodes"])
def get_nodes():
    df = build_dataframe()

    if df.empty:
        return []

    return df.to_dict(orient="records")


@app.get("/summary", tags=["Analytics"])
def summary():
    df = build_dataframe()

    if df.empty:
        return {
            "total_energy": 0.0,
            "avg_power": 0.0,
            "nodes": 0,
            "records": 0
        }

    result = {
        "total_energy": float(df["energy_wh"].sum()),
        "avg_power": float(df["watt"].mean()),
        "nodes": int(df["node_id"].nunique()),
        "records": int(len(df))
    }

    return result


@app.get("/reputation", tags=["Analytics"])
def reputation():
    df = build_dataframe()

    if df.empty:
        return []

    result = []

    for node_id, group in df.groupby("node_id"):
        total_energy = group["energy_wh"].sum()
        stability = group["watt"].std() if len(group) > 1 else 0
        stability = 0 if pd.isna(stability) else stability

        reputation_score = total_energy / (1 + stability)

        result.append({
            "node_id": node_id,
            "reputation": round(float(reputation_score), 2),
            "energy": round(float(total_energy), 2),
            "stability": round(float(stability), 2)
        })

    result.sort(key=lambda x: x["reputation"], reverse=True)
    return result
    