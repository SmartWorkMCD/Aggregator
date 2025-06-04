import sqlite3

DB_NAME = "aggregator.db"

def calculate_metrics():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    metrics = {}

    cursor.execute("SELECT COUNT(*) FROM logs")
    total_logs = cursor.fetchone()[0]
    metrics["total_registos"] = total_logs

    if total_logs == 0:
        return metrics

    cursor.execute("SELECT AVG(assembly_time) FROM logs")
    metrics["tempo_medio_montagem"] = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(defect_count) FROM logs")
    metrics["total_defeitos"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE success = 1")
    success_count = cursor.fetchone()[0]
    metrics["taxa_sucesso"] = (success_count / total_logs) * 100

    cursor.execute("SELECT station_id, COUNT(*) FROM logs GROUP BY station_id")
    metrics["por_estacao"] = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()
    return metrics
