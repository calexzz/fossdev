.PHONY: create-structure test-pytest install install-dep checkdep

create-structure:
	mkdir -p src docs tests
	touch docs/DOMAIN.md
	touch src/.geetkeep tests/.gitkeep
	touch requirements.txt setup.py README.md

install:
	pip install -e .

install-dep:
	pip install -r requirements.txt

checkdep:
	pip install pipreqs


test-pytest:
	pytest
	matplotlib

test: install-dep install test-pytest