format:
	poetry run ruff check --fix sinp_nomenclatures config
	poetry run ruff format sinp_nomenclatures config

lint:
	poetry run ruff check sinp_nomenclatures config

format-check:
	poetry run ruff format --check sinp_nomenclatures config

check: lint format-check

test:
	poetry run python -m manage test

build-docs:
	cd docs && poetry run make html

graph-models:
	poetry run python -m manage graph_models -g --language fr --output models.png  sinp_nomenclatures

docs: build-docs graph-models

fixtures:
	poetry run python -m manage dumpdata --natural-foreign --natural-primary --indent 2 sinp_nomenclatures > sinp_nomenclatures/fixtures/sinp_dict_data_v1.0.json
