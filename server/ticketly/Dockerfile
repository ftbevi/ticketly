FROM python:3.12-slim AS server

ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt update && apt install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
# copiar manifests primeiro pra cache

COPY server/pyproject.toml server/poetry.lock* ./ 

RUN poetry install --only main --no-interaction --no-ansi


FROM python:3.12-slim AS pyruntime

ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN useradd -m app && mkdir -p /app && chown -R app:app /app

RUN apt update && apt install -y --no-install-recommends libpq5 curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=server /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY server/ ./

RUN mkdir -p /app/staticfiles /app/media && chown -R app:app /app

USER app

CMD ["sh", "run.sh"]