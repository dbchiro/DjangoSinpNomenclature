isort:
	poetry run isort sinp_nomenclatures config

black:
	poetry run black sinp_nomenclatures config

flake8:
	poetry run flake8 sinp_nomenclatures config

check: isort black flake8

pylint:
	poetry run pylint --load-plugins pylint_django --django-settings-module=config.settings sinp_nomenclatures config

test:
	poetry run python -m manage test

build-docs:
	cd docs && poetry run make html
