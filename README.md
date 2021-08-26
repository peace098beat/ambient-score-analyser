
# Ambient Analysis
オーディオデータから、Loudness, Sharpness, Rughness を算出するやつ


## インストール

ffmpeg

```sh
❯ brew install ffmpeg
```

python packages

```sh
❯ pip3 install -r requirements.txt
```

amb packages

```sh
❯ pip3 install -e .
```

## 使いかた

example ディレクトリで実行してみよう

```sh
❯ cd example
❯ amb example.wav
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
