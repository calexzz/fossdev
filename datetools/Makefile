VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PACKAGE := datetools

.PHONY: all venv install lint typecheck test build publish-test clean help

all: install lint typecheck test

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

lint: install
	$(PYTHON) -m flake8 $(PACKAGE) tests

typecheck: install
	$(PYTHON) -m mypy $(PACKAGE)

test: install
	$(PYTHON) -m pytest tests/ -v

build: clean install
	$(PYTHON) -m build

publish-test: build
	$(PYTHON) -m twine upload --repository testpypi dist/*

clean:
	rm -rf dist/ build/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete