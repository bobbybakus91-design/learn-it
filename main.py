from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

from ai_engine import run_ai, ai_engine_status, AI_FEATURES


# ============================================================
# LEARN IT API
# ============================================================

app = FastAPI(
    title="Learn It API",
    description="Backend API for Learn It",
    version="1.0.0",
)


# ============================================================
# REQUEST MODEL
# ============================================================

class AIRequest(BaseModel):
    feature: str
    student: dict[str, Any] = {}
    request: str


# ============================================================
# BASIC ROUTES
# ============================================================

@app.get("/")
def home():
    return {
        "app": "Learn It",
        "status": "online",
        "message": "Learn It backend is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ============================================================
# AI ENGINE STATUS
# ============================================================

@app.get("/ai/status")
def ai_status():
    return ai_engine_status()


# ============================================================
# AI FEATURES
# ============================================================

@app.get("/ai/features")
def ai_features():
    return {
        "count": len(AI_FEATURES),
        "features": AI_FEATURES
    }


# ============================================================
# AI REQUEST
# ============================================================

@app.post("/ai")
def ai(request: AIRequest):
    return run_ai(
        feature=request.feature,
        student=request.student,
        request=request.request,
    )
