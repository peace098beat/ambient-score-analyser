import os
import tempfile
import pytest

import monolize

def test_monolize():

	in_file = "./data/1_bouba_woman.wav"

	with tempfile.TemporaryDirectory() as out_dir:

		# [TEST]
		mono_file = monolize.to_mono(in_file=in_file, out_dir=out_dir)

		assert Path(in_file).exists()
		assert Path(mono_file).exists()
		assert Path(out_dir).exists()

	assert Path(mono_file).exists() == False


