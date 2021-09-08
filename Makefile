test1:
	PYTHONPATH=./src pipenv run pytest ./tests/test_pipeline_dir.py

test:
	PYTHONPATH=./src pipenv run pytest ./tests/*

install:
	pipenv run pip install -e .
	amb 1_bouba_woman.wav
	