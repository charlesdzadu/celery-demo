from celery import Celery


app = Celery("queue_worker")

app.config_from_object('celeryconfig')


app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Oslo",
    enable_utc=True,
)

@app.task
def add(x, y):
    # add a delay to simulate a long running task
    import time
    time.sleep(10)
    return x + y
