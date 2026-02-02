from fastapi import FastAPI
import socket
from datetime import datetime, timezone

app = FastAPI(title="DataOps Topic 13 Demo Service")

@app.get("/")
def root():
    return {
        "message": "hello from kubernetes",
        "hostname": socket.gethostname(),
        "utc_time": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
