install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
redo:
	pip install --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
codeclimate:
	codeclimate-test-reporter < coverage.xml
