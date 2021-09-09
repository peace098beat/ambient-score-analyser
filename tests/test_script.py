import os
from pathlib import Path
import script


cwd = os.getcwd()


def test_scrip():
	"""
	test実行時ディレクトリが選択されるため、
	プロジェクトルートでtest実行し、
	cwdをtestsとして指定する.
	"""

	in_dir = "tests/data"
	ext = ".wav"
	out_dir = "tests/outputs"

	in_dir = Path(cwd, in_dir).resolve()
	out_dir = Path(cwd, out_dir).resolve()

	assert Path(in_dir).exists(), in_dir
	assert Path(out_dir).exists(), out_dir

	script.main(in_dir, ext, out_dir)

