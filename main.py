
from fastapi import FastAPI
import queue_worker


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-tasks")
def read_item():
    queue_worker.add.delay(4, 4)
    return {
        "task": "added",
    }
