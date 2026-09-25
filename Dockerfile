FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHOUNBUFFERED=1

ENV POETRY_VERSION=2.2.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=true \
    POETRY_HOME="/opt/poetry/"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        gcc \
        libpq-dev \
    && curl -sSL http://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --no-root --only main

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --no-root --only main

COPY . /app

EXPOSE 8000

RUN useradd -U appuser && chown -R appuser:appuser /app
USER appuser