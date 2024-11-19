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

graph-models:
	poetry run python -m manage graph_models -g --language fr --output models.png  sinp_nomenclatures

docs: build-docs graph-models

fixtures:
	poetry run python -m manage dumpdata --natural-foreign --natural-primary --indent 2 sinp_nomenclatures > sinp_nomenclatures/fixtures/sinp_dict_data_v1.0.json
