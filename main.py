
from fastapi import FastAPI
import queue_worker


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-tasks")
def read_item():
    task = queue_worker.add.delay(4, 4)
    result = task.get(timeout=10, propagate=True)
    return {
        "task": "added",
        "result": result,
    }
