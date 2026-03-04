from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    """Health check endpoint returning status ok."""
    # TODO: Ensure this endpoint returns the expected JSON payload for health monitoring
    return {"status": "ok"}

@app.get("/status")
async def status():
    """Status endpoint returning service metadata."""
    # TODO: Populate service metadata (e.g., name, version, uptime) as per acceptance criteria
    return {
        "service": "MyService",
        "status": "running",
        "version": "1.0.0"
    }
