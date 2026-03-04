from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

# TODO: Add /status endpoint returning service metadata
@app.get("/status")
async def status():
    return {"service": "MyService", "version": "1.0.0"}
