from fastapi import FastAPI, status
import redis
import uvicorn

from config import *


conn = redis.Redis(host=host, port=port, decode_responses=True)

app = FastAPI()


@app.get('/show/{id}')
def show(id):
    return {conn.get(id)}


@app.get('/visit/{id}')
def visit(id):
    conn.incr(id)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info")
