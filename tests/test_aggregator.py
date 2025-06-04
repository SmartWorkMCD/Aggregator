import os
import sqlite3
from datetime import datetime
from data_storage import create_db, insert_log
from aggregator_core import calculate_metrics

TEST_DB = "test_aggregator.db"

def setup_module(module):
    """Setup: Create a fresh test database."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    create_db()

def teardown_module(module):
    """Cleanup: Remove test database after tests."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_insert_log_and_metrics():
    # Simulated input data
    test_data = {
        "station_id": "TEST_STATION",
        "timestamp": datetime.now().isoformat(),
        "assembly_time": 30.5,
        "defect_count": 2,
        "defect_type": "test_defect",
        "success": True
    }

    # Insert the log
    insert_log(test_data)

    # Calculate metrics
    metrics = calculate_metrics()

    # Assertions
    assert "total_registros" in metrics
    assert metrics["total_registros"] >= 1
    assert metrics["tempo_medio_montagem"] > 0
    assert isinstance(metrics["por_estacao"], dict)
