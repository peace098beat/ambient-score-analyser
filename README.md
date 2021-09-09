
# Ambient Analyser
オーディオデータから、Loudness, Sharpness, Rughness を算出するやつ

```
❯ amb data .wav outputs

                 _     _            _   
                | |   (_)          | |  
  __ _ _ __ ___ | |__  _  ___ _ __ | |_ 
 / _` | '_ ` _ \| '_ \| |/ _ \ '_ \| __|
| (_| | | | | | | |_) | |  __/ | | | |_ 
 \__,_|_| |_| |_|_.__/|_|\___|_| |_|\__|


Hello Ambient!
Arthur @peace098beat


Work_dir Dir:/Users/nopara/Codes/ambient-analysis/tests
Input Dir:/Users/nopara/Codes/ambient-analysis/tests/data
Output Dir:/Users/nopara/Codes/ambient-analysis/tests/outputs

be Transforming... 
Plz take a coffee brake :D
Signal resampled to 48 kHz to allow calculation.
Loudness ..
Sharpness ..
Roughness ..
Roughness is being calculated
Signal resampled to 48 kHz to allow calculation.
Loudness ..
Sharpness ..
Roughness ..
Roughness is being calculated


Fin! Check your sounds!  :D



```

## インストール

### 1. Install ffmpeg

```sh
❯ brew install ffmpeg
```

### 2. Install python packages

```sh
❯ pip3 install -r requirements.txt
```

### 3. Install Ambient

```sh
❯ python3 setup.py install
```

## 使いかた

example ディレクトリで実行してみよう

```sh
❯ cd example
❯ amb data .wav outputs
```

以下のようにファイルがたくさんつくられる

```sh
❯ ls
1_bouba_woman.wav 		# 元のファイル

1_bouba_woman.mono.wav	# モノラル & WAV化したファイル
1_bouba_woman.mono.json # 指標の値
1_bouba_woman.mono.jpg  # いい感じにグラフ
1_bouba_woman.mono.pkl	# 謎のファイル
```

指標の値はこんな感じ

```sh
❯ cat 1_bouba_woman.mono.json 
{
  "in_file": "1_bouba_woman.mono.wav",
  "loudness": 0.46851267485012893,
  "sharpness": 0.4473702063504955,
  "roughness": 0.002911119683428289
}
```
