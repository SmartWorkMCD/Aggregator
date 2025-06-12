# Aggregator
Repository for the aggregator microservice of the SmartWorkMCD project 2024/25 UA

## Module Description

### Description:
- Aggregates data and analytics at the last workstation in the assembly line

## Input Data Format
The Aggregator expects JSON data in the following format:

```json
{
  "station_id": "station_23495",
  "timestamp": "2025-05-30T17:41:23.456789",
  "assembly_time": 45.2,
  "defect_count": 2,
  "defect_type": "alignment",
  "success": false
}
```

### Functionality:
- Collects and stores defect rates, assembly times, and performance metrics.
- Generates reports on system efficiency.

### Responsible Members:
- Main Responsible: Inês
- Team: Inês Matos + Pedro Batista

## Running the App

To run the app locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/SmartWorkMCD/Aggregator.git
    cd Aggregator
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run Neighbooring Components (The module migth require another module to be runnning)**
    ```sh
    docker compose up
    ```

5. **Run the app**:
    ```sh
    python3 app/main.py
    ```

6. **Run the API (optional):**
    ```sh
    uvicorn app.api_server:app --reload
    ```
    - Access the endpoint directly: http://127.0.0.1:8000/metrics
    - Access the docs: http://127.0.0.1:8000/docs


7. **Run the data collector (optional):**
    ```sh
    python app/data_collector.py
    ```

    - The service will listen on port 5001 for incoming JSON data from workstations.
