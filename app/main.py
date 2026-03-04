from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "ok"}

# TODO: Add tests for /health endpoint

@app.get("/status")
def status():
    """Service metadata endpoint"""
    return {"service": "MyService", "version": "1.0.0", "description": "Service metadata"}

# TODO: Add tests for /status endpoint
