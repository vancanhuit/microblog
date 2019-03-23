web: flask db upgrade; gunicorn main:application
worker: rq worker -u $REDIS_URL microblog-tasks
