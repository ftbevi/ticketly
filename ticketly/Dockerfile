FROM python:3.13-slim AS server

ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev libpq5 curl

RUN apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY ticketly/ .

RUN poetry config virtualenvs.create false && \
    poetry install --only=main --no-root

EXPOSE 8000

RUN chmod +x run.sh

CMD ["sh", "run.sh"]
