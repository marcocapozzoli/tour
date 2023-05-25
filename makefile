create-migrations:
	@python src/infra/manage.py makemigrations

apply-migrations:
	@python src/infra/manage.py migrate

run-app:
	@python src/infra/manage.py runserver

isort:
	@isort src --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

black:
	@black src --line-length 79 -t py37 --skip-string-normalization

flake8:
	@flake8 --show-source src

lint: isort black flake8

test-cov:
	@poetry run pytest -x --cov=src/ --cov-report=term-missing --cov-fail-under=80

up:
	docker-compose up

up_d:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

all: down build up