from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    """
    Health check endpoint.
    """
    # TODO: Ensure the endpoint returns status ok as per acceptance criteria
    return JSONResponse(content={"status": "ok"})

@app.get("/status")
def status():
    """
    Service metadata endpoint.
    """
    # TODO: Return service metadata as per acceptance criteria
    metadata = {
        "service": "MyService",
        "version": "1.0.0",
        "description": "Service metadata"
    }
    return JSONResponse(content=metadata)
