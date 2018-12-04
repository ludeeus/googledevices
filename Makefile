init:
	pip install --upgrade pip pipenv
	pipenv lock
	pipenv install --dev
lint:
	pipenv run flake8 googledevices
	pipenv run pydocstyle googledevices
	pipenv run pylint --disable=R0205,R0903,I1101,R0801 googledevices
test:
	pipenv run py.test
typing:
	pipenv run mypy --ignore-missing-imports googledevices