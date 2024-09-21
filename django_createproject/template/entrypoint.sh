#!/bin/bash

# logs
if [ ! -d "logs" ]; then
    mkdir logs
    chmod -R 777 logs
fi

# migrate & static
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# run
gunicorn --access-logfile - \
    --workers 3 \
    --bind 0.0.0.0:$API_PORT \
    -k uvicorn.workers.UvicornWorker \
    config.asgi:application
