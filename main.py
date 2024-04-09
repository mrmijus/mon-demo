from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn


app = FastAPI()

Instrumentator().instrument(app).expose(app) 

@app.get("/healthcheck")
def health():
    return {'message': "HEALTH: OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
