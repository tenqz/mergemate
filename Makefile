.PHONY: check lint test

lint:
	poetry run ruff check src

test:
	poetry run pytest

check: lint test
