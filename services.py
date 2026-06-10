from db import get_connection
from schemas import NodeIngestPayload


def ingest_node_data(payload: NodeIngestPayload) -> dict:
    row = (
        int(payload.timestamp),
        payload.node_id,
        payload.watt,
        payload.energy_wh
    )

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO node_data (
                timestamp, node_id, watt, energy_wh
            ) VALUES (?, ?, ?, ?)
        """, row)
        conn.commit()

    return {
        "status": "ok",
        "message": "Dato nodo salvato correttamente",
        "node_id": payload.node_id
    }


def get_nodes_data() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT timestamp, node_id, watt, energy_wh
            FROM node_data
            ORDER BY timestamp ASC
        """).fetchall()

    return [dict(r) for r in rows]


def get_summary_data() -> dict:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT
                SUM(energy_wh) AS total_energy,
                AVG(watt) AS avg_power,
                COUNT(DISTINCT node_id) AS nodes,
                COUNT(*) AS records
            FROM node_data
        """).fetchone()

    return {
        "total_energy": row["total_energy"] or 0.0,
        "avg_power": row["avg_power"] or 0.0,
        "nodes": row["nodes"] or 0,
        "records": row["records"] or 0
    }


def get_reputation_data() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT
                node_id,
                SUM(energy_wh) AS energy,
                COALESCE(STDDEV(watt), 0) AS stability
            FROM node_data
            GROUP BY node_id
        """).fetchall()

    result = []

    for r in rows:
        energy = r["energy"] or 0.0
        stability = r["stability"] or 0.0

        reputation = energy / (1 + stability)

        result.append({
            "node_id": r["node_id"],
            "energy": round(float(energy), 2),
            "stability": round(float(stability), 2),
            "reputation": round(float(reputation), 2)
        })

    result.sort(key=lambda x: x["reputation"], reverse=True)
    return result