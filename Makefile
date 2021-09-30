test:
	pipenv run pip install .
	pipenv run amb --help
	pipenv run pip uninstall amb

install:
	pipenv run pip install .

local-test:
	PYTHONPATH=./src pipenv run pytest ./tests/*

local-install:
	pipenv run pip install -e .

release:
	pipenv run autopep8 --in-place ./src/amb/*.py
	pipenv run autopep8 --in-place ./tests/*.py
	pipenv run flake8 ./src/amb --count --select=E9,F63,F7,F82 --show-source --statistics
	pipenv run flake8 ./src/amb --count --exit-zero --max-complexity=10 --max-line-length=127 #make--statistics