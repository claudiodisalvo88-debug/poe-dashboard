from fastapi import FastAPI
from db import read_data
import pandas as pd

app = FastAPI(title="PoE API")

@app.get("/")
def home():
    return {"status": "PoE API running"}

@app.get("/nodes")
def get_nodes():
    data = read_data()

    df = pd.DataFrame(data, columns=[
        "timestamp",
        "node_id",
        "watt",
        "energy_wh"
    ])

    return df.to_dict(orient="records")


@app.get("/summary")
def summary():
    data = read_data()

    df = pd.DataFrame(data, columns=[
        "timestamp",
        "node_id",
        "watt",
        "energy_wh"
    ])

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    result = {
        "total_energy": float(df["energy_wh"].sum()),
        "avg_power": float(df["watt"].mean()),
        "nodes": int(df["node_id"].nunique()),
        "records": len(df)
    }

    return result


@app.get("/reputation")
def reputation():
    data = read_data()

    df = pd.DataFrame(data, columns=[
        "timestamp",
        "node_id",
        "watt",
        "energy_wh"
    ])

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    result = []

    for node_id, group in df.groupby("node_id"):
        total_energy = group["energy_wh"].sum()
        stability = group["watt"].std() if len(group) > 1 else 0
        stability = 0 if pd.isna(stability) else stability

        reputation = total_energy / (1 + stability)

        result.append({
            "node_id": node_id,
            "reputation": round(reputation, 2),
            "energy": round(total_energy, 2),
            "stability": round(stability, 2)
        })

    return result
	