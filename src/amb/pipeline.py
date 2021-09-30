"""
    main.py

    :usage:
    > python main.py --target ../data/1_test.wav --outdir ../outputs

"""
from pathlib import Path

from . import monolizer
from . import featurizer

from logging import getLogger
logger = getLogger(__name__)

logger.debug(__name__)

def run(in_file):
    
    # 1. Monolize
    try:
        mono_file = monolizer.to_mono(in_file)
    except KeyboardInterrupt:
        return []

    # 2. Featurize
    try:
        fig_path, json_path, sig_path = featurizer.run(mono_file)
    except KeyboardInterrupt:
        return [mono_file]

    outputs = [
        mono_file,
        fig_path,
        json_path,
        sig_path
    ]

    return outputs

import glob
import shutil
def run_dir(in_dir, ext, out_dir):

    assert Path(in_dir).exists(), in_dir
    assert ext.startswith("."), ext

    audio_p_s = glob.glob(f"{str(in_dir)}/*{ext}")

    N = len(list(audio_p_s))
    assert N > 0

    out_files_s = []
    dist_files_s = []

    try:
        for n, audio_p in enumerate(audio_p_s):

            logger.debug(f"[{n}/{N}]: {audio_p}")

            out_files = run(audio_p)

            out_files_s += out_files

        for out_file in out_files_s:
            assert Path(out_file).exists(), out_file
            dist_p = Path(out_dir) / Path(out_file).name
            a = shutil.move(out_file, dist_p)
            assert Path(a).exists(), a
            dist_files_s.append(a)

    except KeyboardInterrupt:
        rm_files = out_files_s + dist_files_s
        print(rm_files)
        for rm_file in rm_files:
            if Path(rm_file).exists():
                Path(rm_file).unlink()

        import sys
        sys.exit(0)



    return out_files_s


