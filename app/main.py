from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

# TODO: Ensure status endpoint returns correct service metadata
@app.get("/status")
async def status():
    return {"service": "my_service", "version": "1.0.0"}
