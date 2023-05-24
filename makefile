create-migrations:
	@python src/manage.py makemigrations

apply-migrations:
	@python src/manage.py migrate

run-app:
	@python src/manage.py runserver

isort:
	@isort src --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

black:
	@black src --line-length 79 -t py37 --skip-string-normalization

flake8:
	@flake8 --show-source src

lint: isort black flake8