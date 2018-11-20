from celery import Celery

# app = Celery('app',
#              broker='redis://127.0.0.1:6379/1',
#              backend='redis://127.0.0.1:6379/2'
# )


app =  Celery('app')
app.config_from_object('celery_conf')


@app.task
def task_one():
    print('哈哈哈')