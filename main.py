
from fastapi import FastAPI
import queue_worker


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-tasks")
def read_item():
    # Add 100 tasks to the queue
    for i in range(100):
        queue_worker.add.delay(i, i)
    return {
        "task": "added",
    }
