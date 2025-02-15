create_app:
	python3 manage.py startapp apps

run:
	python3 manage.py runserver --insecure localhost:8000

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

create_user:
	python3 manage.py createsuperuser

lang:
	python3 manage.py makemessages -l uz
	python3 manage.py makemessages -l ru
	python3 manage.py makemessages -l en
