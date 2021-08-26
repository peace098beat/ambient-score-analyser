"""
    main.py

    :usage:
    > python main.py --target ../data/1_test.wav --outdir ../outputs

"""
import argparse

import monolizer
import featurizer


def run(in_file):
    
    # 1. Monolize
    mono_file = monolizer.to_mono(in_file)

    # 2. Featurize
    fig_path, json_path, sig_path = featurizer.run(mono_file)

    outputs = [
        mono_file,
        fig_path,
        json_path,
        sig_path
    ]

    return outputs


# def get_arg():
#     parser = argparse.ArgumentParser(description='ambient analyser')
#     parser.add_argument('--in_file', help='オーディオファイル')
#     args = parser.parse_args()
#     print('in_file='+args.in_file)
#     return args

# if __name__ == '__main__':
#     args = get_arg()
#     main(args.in_file, args.out_dir)
