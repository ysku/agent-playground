from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    """
    Health check endpoint that returns the status of the application.
    
    Returns:
        dict: A JSON response with status "ok"
    """
    return {"status": "ok"}
