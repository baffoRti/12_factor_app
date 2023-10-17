from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values


config = dotenv_values(".env")
conn = redis.from_url(f'redis://{config["host_redis"]}:{config["port_redis"]}')

app = FastAPI()


@app.get('/show/{id}')
def show(id):
    return {conn.get(id)}


@app.get('/visit/{id}')
def visit(id):
    conn.incr(id)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app,host = config["host"], port = config['site_port'], log_level = config['log_level'])
