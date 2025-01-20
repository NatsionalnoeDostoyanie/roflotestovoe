.PHONY: install-base install-full lint format-code

install-base:
	poetry install --no-dev

install-full:
	poetry install

lint:
	poetry run mypy .

format-code:
	poetry run autoflake . && poetry run isort . && poetry run black .

run-calculator:
	poetry run python src/calculator/operators.py

run-factorial:
	poetry run python src/factorial/factorial.py

run-infinite-array:
	poetry run python src/infinite_array/infinite_array.py

run-sortirovka-massiva:
	poetry run python src/sortirovka_massiva/glavnyi.py
