.PHONY: check lint test docstyle doccov

lint:
	poetry run ruff check src tests

test:
	poetry run pytest

docstyle:
	poetry run pydocstyle src tests

doccov:
	poetry run interrogate --generate-badge badges/doc_coverage.svg src tests

check:
	$(MAKE) lint
	$(MAKE) test
	$(MAKE) docstyle
	$(MAKE) doccov
