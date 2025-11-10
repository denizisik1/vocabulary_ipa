.PHONY: format lint typecheck security test check

format:
	black --line-length 100 src tests

lint:
	flake8 --max-line-length 100 src tests
	pylint src

typecheck:
	mypy src tests

security:
	bandit -r src

test:
	pytest -v --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing

check: format lint typecheck security test
