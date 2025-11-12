.PHONY: check lint test docstyle doccov

lint:
	poetry run ruff check src

test:
	poetry run pytest

docstyle:
	poetry run pydocstyle src

doccov:
	poetry run interrogate --generate-badge badges/doc_coverage.svg src

check:
	$(MAKE) lint
	$(MAKE) test
	$(MAKE) docstyle
	$(MAKE) doccov
