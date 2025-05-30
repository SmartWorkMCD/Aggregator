from fastapi import FastAPI
from aggregator_core import calculate_metrics

app = FastAPI(
    title="Smart Work Aggregator API",
    description="API to expose aggregated station metrics",
    version="1.0.0"
)

@app.get("/metrics")
def get_metrics():
    """
    Returns the aggregated metrics calculated by the Aggregator.
    """
    return calculate_metrics()
