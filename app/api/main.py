from fastapi import FastAPI

app = FastAPI(
    title="Bank Marketing MLOps API",
    description="Docker-based DataOps and MLOps platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "Bank Marketing MLOps",
        "status": "running",
        "environment": "Docker"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "FastAPI"
    }