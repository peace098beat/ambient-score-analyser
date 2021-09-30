import glob
import json
from pathlib import Path
import numpy as np

from matplotlib import pyplot as plt
import japanize_matplotlib


def _load_json(json_path):

    with open(json_path, mode='rt', encoding='utf-8') as fp:
        data = json.load(fp)
    return data


def post_process(out_dir):

    json_paths = glob.glob(f"{out_dir}/*.json")

    datas = []
    for json_path in json_paths:
        data = _load_json(json_path)

        in_file = data["in_file"]
        loudness = data["loudness"]
        sharpness = data["sharpness"]
        roughness = data["roughness"]

        datas.append(data)

    colorlist = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
                 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
    y_feature = "loudness"
    x_features = ["sharpness", "roughness"]

    plt.rcParams["font.size"] = 14

    fig, ax = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
    axs = ax.flatten()

    for ax_no in [0, 1]:

        plt.sca(axs[ax_no])

        for i, data in enumerate(datas):
            in_file = data["in_file"]

            wav_name = in_file.split("/")[-1]

            x_feature = x_features[ax_no]
            x = data[x_feature]
            y = data[y_feature]

            if len(datas) <= len(colorlist):

                c = colorlist[i]
            else:
                c = "tab:orange"

            plt.plot(x, y, "o", markersize=10, color=c,
                     label=wav_name, alpha=0.75)
            plt.text(x, y, wav_name, color="#000000",
                     fontfamily="serif",
                     # fontweight="bold",
                     fontstyle="italic",
                     fontsize=12)

        # axs[0].set_xlim([0, 6])
        # axs[0].set_ylim([0, 21])
        # axs[1].set_xlim([-0.1, 0.7])
        plt.tight_layout()
        plt.ylabel(y_feature)
        plt.xlabel(x_feature)
        plt.grid()

    plt.savefig(Path(out_dir) / f"Loudness-vs-Sharpnes-Roghness.jpg")
