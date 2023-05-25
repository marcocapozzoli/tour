# Use an official Python runtime
FROM python:3.11.0

# Data authors and maintainers 
LABEL maintainer="Marco Capozzoli"
LABEL author="Marco Capozzoli <marcocapozzoli90@gmail.com>"

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p app/

# Install system packages required by Django.
RUN set -x; apt-get update --yes --quiet \
        && apt-get install --yes --quiet --no-install-recommends \
        postgresql-client \
        && rm -rf /var/lib/apt/lists/*

# Create group and add user "django"
RUN set -x; \
        groupadd -r -g 999 django \
        && adduser --system --home=/app/ django --uid 999 --gid 999

# Install the project requirements.
# COPY  ./requirements.txt /code/requirements.txt
# RUN set -x; pip install -r /code/requirements.txt

RUN pip3 install poetry

COPY ./pyproject.toml app/

# Use /code folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "django" user. This Django Project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN set -x; chown django:django /app

# Copy the source code of the project into the container.
COPY --chown=django:django . .

# Use user "django" to run the build commands below and the server itself.
USER django

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY ./entrypoint.sh /
COPY ./run_app.sh /
