FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

#RUN pip install poetry && \
#    poetry export -f requirements.txt --output requirements.txt && \
#    pip install -r requirements.txt
RUN pip install poetry &&  \
    poetry install --only main --no-root && \
    rm -rf $POETRY_CACHE_DIR

COPY . /app

CMD ["gunicorn", "web:asgi_app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]
