FROM python:3.11.0

RUN apt-get update && apt-get install -y postgresql-client

ENV PYTHONUNBUFFERED 1

RUN mkdir -p app/

RUN pip3 install poetry

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY ./pyproject.toml app/

WORKDIR /app

RUN poetry config virtualenvs.create false

RUN poetry install --only main