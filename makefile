create-migrations:
	@python src/manage.py makemigrations

apply-migrations:
	@python src/manage.py migrate

run-app:
	@python src/manage.py runserver