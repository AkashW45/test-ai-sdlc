from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """Health check endpoint returning status ok"""
    return {"status": "ok"}

@app.get("/status")
def status():
    """Status endpoint returning service metadata"""
    # TODO: Populate with actual service metadata (e.g., name, version, uptime)
    return {
        "service": "MyService",
        "version": "1.0.0",
        "status": "running"
    }
