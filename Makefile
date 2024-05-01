.PHONY: clean
clean:
	poetry run pyclean src/brokkr tests

.PHONY: install
install:
	poetry install --with dev --no-root

.PHONY: test
test:
	poetry run pytest tests -W ignore::DeprecationWarning

.PHONY: build
build:
	poetry build --format wheel

.PHONY: clean-test
clean-test: clean test
