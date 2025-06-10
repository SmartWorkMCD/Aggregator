# API SERVER

from fastapi import FastAPI
from .aggregator_core import calculate_metrics
from .data_storage import insert_log, create_db
from pydantic import BaseModel

create_db()

app = FastAPI(
    title="Smart Work Aggregator API",
    description="API to expose aggregated station metrics",
    version="1.0.0"
)

class DataInput(BaseModel):
    station_id: str
    timestamp: str
    assembly_time: float
    defect_count: int
    defect_type: str
    success: bool

@app.get("/metrics")
def get_metrics():
    """
    Returns the aggregated metrics calculated by the Aggregator.
    """
    return calculate_metrics()

@app.post("/data")
def post_data(data: DataInput):
    print("Received data: ")
    print(data.model_dump())
    return {"success": insert_log(data.model_dump())}