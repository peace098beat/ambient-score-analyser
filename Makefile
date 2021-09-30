local-test:
	PYTHONPATH=./src pipenv run pytest ./tests/*


test:
	pipenv run pip install .
	pipenv run amb --help
	pipenv run pip uninstall amb

install:
	pipenv run pip install .

local-install:
	pipenv run pip install -e .
	