from pathlib import Path

import subprocess


def to_mono(in_file):

    in_file = str(in_file)

    out_path = Path(in_file).with_suffix(".mono.wav")

    subprocess.call(['ffmpeg', '-i', in_file, '-ac', "1", "-ar", "44100", "-loglevel", "panic",
                     str(out_path)])

    return out_path
