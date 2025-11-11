FROM python:3.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    ca-certificates \
 && update-ca-certificates \
 && pip install poetry \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
RUN poetry install --with dev --no-root

COPY src ./src
COPY tests ./tests

CMD ["poetry", "run", "python", "-m", "mergemate.main"]
