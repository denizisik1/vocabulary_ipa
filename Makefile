# To prevent confusion with filenames, all targets are declared as phony.
.PHONY: format lint typecheck security test check

a format:
	black --line-length 100 src tests

b lint:
	flake8 --max-line-length 100 src tests
	pylint src tests

c typecheck:
	mypy src tests

d security:
	bandit -r src tests

e test:
	pytest -v --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing

x check: format lint typecheck security test
