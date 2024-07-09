# flask-boilerplate

## Local run

```shell
flask --app web run
# or
FLASK_APP=web flask run
```

## Lint

```shell
ruff check .
```

## Deploy

synchronize: Gunicorn
async: Hypercorn/uvcorn

```shell
pip install "uvicorn[standard]" gunicorn
````

Note: on MacOS. Run this command to fix gunicorn error

```shell
export NO_PROXY=*
```

```shell
hypercorn web:asgi_app

uvicorn web:asgi_app --host 0.0.0.0 --port 80

gunicorn web:asgi_app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```
