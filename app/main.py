from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    """Health endpoint returning a simple status.

    TODO: Ensure /health returns status ok as per acceptance criteria.
    """
    return {"status": "ok"}


@app.get("/status")
async def status():
    """Status endpoint returning service metadata.

    TODO: Return appropriate service metadata (e.g., version, name, uptime) as per acceptance criteria.
    """
    # Placeholder metadata; replace with actual values if needed.
    return {
        "service": "MyService",
        "version": "1.0.0",
        "status": "running"
    }
