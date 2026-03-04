from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    """TODO: Return health status"""
    return {"status": "ok"}

@app.get("/status")
async def status():
    """TODO: Return service metadata"""
    return {"service": "MyService", "version": "1.0.0"}
