from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI instance.
    """
    app = FastAPI()

    @app.get("/health")
    async def health() -> dict:
        """Health check endpoint.

        Returns:
            dict: Simple status payload indicating the service is healthy.
        """
        # TODO: Ensure health endpoint returns status ok as per acceptance criteria
        return {"status": "ok"}

    @app.get("/status")
    async def status() -> dict:
        """Status endpoint returning service metadata.

        Returns:
            dict: Metadata about the service (e.g., name, version).
        """
        # TODO: Populate service metadata according to acceptance criteria
        return {
            "service": "MyService",
            "version": "1.0.0"
        }

    return app


app = create_app()
