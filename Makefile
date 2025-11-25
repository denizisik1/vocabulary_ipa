# To prevent confusion with filenames, all targets are declared as phony.
.PHONY: format lint typecheck security test check a b c d e f all

a format:
	black --line-length 100 src tests

b flake8:
	flake8 --max-line-length 100 src tests

c pylint:
	pylint --disable=missing-class-docstring,missing-function-docstring,missing-module-docstring src tests

d typecheck:
	mypy src tests

e security:
	bandit -r src tests

f test:
	pytest

all check: format flake8 pylint typecheck security test
