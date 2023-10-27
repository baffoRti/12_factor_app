"""Pylint ацтань x1"""
from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values


config = dotenv_values(".env")
conn = redis.from_url(f'redis://{config["host_redis"]}:{config["port_redis"]}')

app = FastAPI()


@app.get('/show/{id_par}')
def show(id_par):
    """Pylint ацтань x2"""
    return {conn.get(id_par)}


@app.get('/visit/{id_par}')
def visit(id_par):
    """Pylint ацтань x3"""
    conn.incr(id_par)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app,host = config["host"], port = config['site_port'], 
                log_level = config['log_level'])
