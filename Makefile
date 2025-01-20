.PHONY: install-base install-full lint format-code

install-base:
	poetry install --no-dev

install-full:
	poetry install

lint:
	poetry run mypy .

format-code:
	poetry run autoflake . && poetry run isort . && poetry run black .
