# test_pipeline_dir.py

from pathlib import Path
import tempfile
import shutil

import pytest
from amb import pipeline


work_dir = Path(__file__).parent.resolve()


def test_pipeline_dir():

    in_dir = "data"
    ext = "wav"
    out_dir = "outputs/test_pipeline_dir"


    # Setup in_dir
    in_dir = Path(work_dir, in_dir)
    assert Path(in_dir).exists()

    # Setup ext
    if not ext.startswith("."):
        ext = f".{ext}"

    # Setup OutDir
    out_dir = Path(work_dir) / out_dir

    if Path(out_dir).exists():
        shutil.rmtree(out_dir)
    assert Path(out_dir).exists() == False

    Path(out_dir).mkdir(exist_ok=True, parents=True)
    assert Path(out_dir).exists(), out_dir

    n_audios = len(list(Path(in_dir).glob(f"*{ext}")))
    assert n_audios > 0

    # TEST
    pipeline.run_dir(in_dir, ext, out_dir)

    n_outfiles = len(list(Path(out_dir).glob(f"*")))
    assert n_outfiles > 0

    n_mono = len(list(Path(out_dir).glob("*.mono.*")))
    assert n_audios == n_mono / 4

    n_json = len(list(Path(out_dir).glob("*.json")))
    assert n_audios == n_json


if __name__ == '__main__':
    print(__FILE__)