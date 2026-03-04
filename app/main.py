from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    """Health check endpoint returning status ok.
    TODO: Verify that the endpoint returns {"status": "ok"} with HTTP 200.
    """
    return {"status": "ok"}

@app.get("/status")
async def status():
    """Service status endpoint returning metadata.
    TODO: Verify that the endpoint returns {"service": "MyService", "version": "1.0.0", "status": "running"} with HTTP 200.
    """
    return {"service": "MyService", "version": "1.0.0", "status": "running"}
