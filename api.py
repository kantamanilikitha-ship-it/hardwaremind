from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from hardware_agent import (
    investigate_failure,
    learn_from_confirmed_resolution
)


app = FastAPI(
    title="HardwareMind API",
    description="AI Hardware Failure Investigation Backend",
    version="1.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# FAILURE REQUEST
# ============================================================

class FailureRequest(BaseModel):
    incident_id: str
    device: str
    device_type: str
    temperature: float
    voltage: float
    current: float
    symptoms: str
    sensor_status: str
    communication_status: str


# ============================================================
# LEARNING REQUEST
# ============================================================

class LearningRequest(BaseModel):
    incident_id: str
    device: str
    device_type: str
    temperature: float
    voltage: float
    current: float
    symptoms: str
    sensor_status: str
    communication_status: str

    confirmed_root_cause: str
    confirmed_fix: str
    outcome: str


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "online",
        "service": "HardwareMind API"
    }


# ============================================================
# INVESTIGATE FAILURE
# ============================================================

@app.post("/investigate")
def investigate(request: FailureRequest):

    incident = request.model_dump()

    result = investigate_failure(incident)

    return {
        "success": True,
        "diagnosis": result["diagnosis"],
        "memory_context": result["memory_context"]
    }


# ============================================================
# LEARN FROM CONFIRMED RESOLUTION
# ============================================================

@app.post("/learn")
def learn(request: LearningRequest):

    incident = {
        "incident_id": request.incident_id,
        "device": request.device,
        "device_type": request.device_type,
        "temperature": request.temperature,
        "voltage": request.voltage,
        "current": request.current,
        "symptoms": request.symptoms,
        "sensor_status": request.sensor_status,
        "communication_status": request.communication_status
    }

    result = learn_from_confirmed_resolution(
        incident,
        request.confirmed_root_cause,
        request.confirmed_fix,
        request.outcome
    )

    return {
        "success": True,
        "message": "HardwareMind learned from the confirmed resolution.",
        "result": result
    }