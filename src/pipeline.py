"""
    main.py

    :usage:
    > python main.py --target ../data/1_test.wav --outdir ../outputs

"""
import argparse


import monolize

def get_arg():

    parser = argparse.ArgumentParser(description='ambient analyser')

    parser.add_argument('--in_file', help='オーディオファイル')
    parser.add_argument('--out_dir', help='出力先ディレクトリ')

    args = parser.parse_args()

    print('in_file='+args.in_file)
    print('out_dir='+args.out_dir)

    return args


def run(in_file, out_dir):
    
    Path.mkdir(out_file, exist_ok=True, parents=True)

    out_file = Path(out_dir) / Path(in_file).name

    # 作業ディレクトリ

    mono_file = monolize.to_mono(in_file, out_dir)

    # pipeline 処理




if __name__ == '__main__':
    
    args = get_arg()

    main(args.in_file, args.out_dir)




