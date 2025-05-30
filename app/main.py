from data_storage import create_db, insert_log
from aggregator_core import calculate_metrics
from datetime import datetime

def main():
    create_db()  

    # Simulated input data
    dummy_data = {
        "station_id": "WS_1",
        "timestamp": datetime.now().isoformat(),
        "assembly_time": 45.2,
        "defect_count": 1,
        "defect_type": "misalignment",
        "success": False
    }

    insert_log(dummy_data)

    # Show metrics
    metrics = calculate_metrics()
    print("Aggregated metrics:", metrics)

if __name__ == "__main__":
    main()

