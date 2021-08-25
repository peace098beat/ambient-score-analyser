from pathlib import Path

import pytest
import pipeline


def test_run():

	in_file = "./data/1_bouba_woman.wav"
	out_dir = "./outputs/"
	out_file = Path(out_dir) / Path(in_file).name

	assert Path(in_file).exists()

	assert out_file == "./outputs/1_bouba_woman.wav"

	pipeline.run(in_file=in_file, out_dir=out_dir)

	assert Path(out_dir).exists()
	assert Path(out_file).exists()


if __name__ == '__main__':
	print(__FILE__)