init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run python manage.py test

ci:
	pipenv run python manage.py test

isort:
	isort --recursive --settings-path ./setup.cfg .

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 --exclude=./node_modules
