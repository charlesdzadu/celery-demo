import settings as s

broker_url = f"{s.settings.REDIS_URL}/0"
result_backend = f"{s.settings.REDIS_URL}/0"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
broker_connection_retry_on_startup = True






task_annotations = {
    'queue_worker.add': {'rate_limit': '10/m'}
}
