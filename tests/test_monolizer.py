import os
import tempfile
from pathlib import Path

import pytest

import monolizer

def test_monolize():

	in_file = "data/1_bouba_woman.wav"
	in_file = Path(__file__).parent / in_file
	in_file = in_file.resolve()

	assert Path(in_file).exists()

	# [TEST]
	mono_file = monolizer.to_mono(in_file=in_file)

	assert Path(mono_file).exists() == True

	Path(mono_file).unlink()

	assert Path(mono_file).exists() == False



