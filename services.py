import pandas as pd
from datetime import datetime

from db import get_connection, read_data
from schemas import NodeIngestPayload


def ingest_node_data(payload: NodeIngestPayload) -> dict:
    try:
        ts = payload.timestamp

        if isinstance(ts, str):
            try:
                ts = int(datetime.fromisoformat(ts).timestamp())
            except:
                ts = int(datetime.now().timestamp())

        row = (
            int(ts),
            payload.node_id,
            payload.watt,
            payload.energy_wh
        )

        with get_connection() as conn:
            conn.execute("""
                INSERT OR IGNORE INTO node_data (
                    timestamp,
                    node_id,
                    watt,
                    energy_wh
                ) VALUES (?, ?, ?, ?)
            """, row)
            conn.commit()

        return {
            "status": "ok",
            "message": "Dato nodo salvato correttamente",
            "node_id": payload.node_id
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "node_id": getattr(payload, "node_id", None)
        }


def build_dataframe() -> pd.DataFrame:
    data = read_data()

    df = pd.DataFrame(
        data,
        columns=["timestamp", "node_id", "watt", "energy_wh"]
    )

    if df.empty:
        return df

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
    df = df.dropna(subset=["timestamp"])

    return df


def get_nodes_data() -> list[dict]:
    df = build_dataframe()
    if df.empty:
        return []
    return df.to_dict(orient="records")


def get_summary_data() -> dict:
    df = build_dataframe()

    if df.empty:
        return {
            "total_energy": 0.0,
            "avg_power": 0.0,
            "nodes": 0,
            "records": 0
        }

    return {
        "total_energy": float(df["energy_wh"].sum()),
        "avg_power": float(df["watt"].mean()),
        "nodes": int(df["node_id"].nunique()),
        "records": int(len(df))
    }


def get_reputation_data() -> list[dict]:
    df = build_dataframe()

    if df.empty:
        return []

    result = []

    for node_id, group in df.groupby("node_id"):
        total_energy = group["energy_wh"].sum()
        stability = group["watt"].std() if len(group) > 1 else 0
        stability = 0 if pd.isna(stability) else stability

        score = total_energy / (1 + stability)

        result.append({
            "node_id": node_id,
            "reputation": round(float(score), 2),
            "energy": round(float(total_energy), 2),
            "stability": round(float(stability), 2)
        })

    result.sort(key=lambda x: x["reputation"], reverse=True)
    return result
