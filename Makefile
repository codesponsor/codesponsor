init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run python manage.py test

ci:
	pipenv run python manage.py test

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821
