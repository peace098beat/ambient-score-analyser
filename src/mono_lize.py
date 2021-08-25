from pathlib import Path
# import numpy as np
# import pandas as pd

import warnings
warnings.simplefilter('ignore')

# DATA1_DIR = "../data/01_raw/3_dataset"
# OUT1_DIR = "../data/01_raw/3_dataset_mono/"

# wav1_paths = [str(p) for p in list(Path(DATA1_DIR).glob("*.wav")) ]
# wav1_paths.sort()


def convert_mono(snd_path, out_dir):
    import subprocess
    Path(out_dir).mkdir(exist_ok=True, parents=True)
    
    out_path = Path(out_dir) / Path(snd_path).name
    
    out_path = Path(out_path).with_suffix(".mono.wav")
    subprocess.call(['ffmpeg', '-i', snd_path, '-ac', "1", "-ar", "44100",
                str(out_path)])
    
    return out_path


# for wav_p in wav1_paths:
#     w = convert_mono(wav_p, OUT1_DIR, )
#     print(w)
    
