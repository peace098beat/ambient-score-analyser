from pathlib import Path
import tempfile

import pytest
from amb import pipeline


def test_pipeline():

	in_file = "data/1_bouba_woman.wav"
	in_file = Path(__file__).parent / in_file
	in_file = in_file.resolve()

	assert Path(in_file).exists()

	# TEST
	outputs = pipeline.run(in_file=in_file)

	mono_file,fig_path,json_path, sig_path = outputs

	assert Path(mono_file).exists()
	assert Path(fig_path).exists()
	assert Path(json_path).exists()
	assert Path(sig_path).exists()

	Path(mono_file).unlink()
	Path(fig_path).unlink()
	Path(json_path).unlink()
	Path(sig_path).unlink()

	assert Path(mono_file).exists() == False
	assert Path(fig_path).exists() == False
	assert Path(json_path).exists() == False
	assert Path(sig_path).exists() == False

if __name__ == '__main__':
	print(__FILE__)