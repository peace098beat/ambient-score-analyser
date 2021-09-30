import os
from pathlib import Path

import pytest

from amb import monolizer
from amb import featurizer

def test_featurizer():

	in_file = "data/1_bouba_woman.wav"
	in_file = Path(__file__).parent / in_file
	in_file = in_file.resolve()

	assert Path(in_file).exists()

	# [TEST]
	mono_file = monolizer.to_mono(in_file=in_file)
	assert Path(mono_file).exists()

	fig_path, json_path, sig_path = featurizer.run(in_file=mono_file)

	assert Path(fig_path).exists()
	assert Path(json_path).exists()
	assert Path(sig_path).exists()


	# Clearn Up
	Path(mono_file).unlink()
	Path(fig_path).unlink()
	Path(json_path).unlink()
	Path(sig_path).unlink()

	assert Path(mono_file).exists() == False
	assert Path(fig_path).exists() == False
	assert Path(json_path).exists() == False
	assert Path(sig_path).exists() == False


