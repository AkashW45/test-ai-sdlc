from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

# TODO: Verify status endpoint returns correct service metadata
@app.get("/status")
async def status():
    return {"service": "myservice", "version": "1.0.0"}
