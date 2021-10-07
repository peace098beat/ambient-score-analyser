import os
from pathlib import Path
import shutil
import click
from . import pipeline
from . import post_process


banner = '''
                 _     _            _   
                | |   (_)          | |  
  __ _ _ __ ___ | |__  _  ___ _ __ | |_ 
 / _` | '_ ` _ \| '_ \| |/ _ \ '_ \| __|
| (_| | | | | | | |_) | |  __/ | | | |_ 
 \__,_|_| |_| |_|_.__/|_|\___|_| |_|\__|

'''

work_dir = Path(".").parent.resolve()


# @click.command()
# @click.argument('in_dir')
# def _(in_dir):

#     cwd = os.getcwd()

#     in_dir = Path(cwd, in_dir).resolve()
#     assert Path(in_dir).exists(), in_dir

#     out_dir = Path(cwd, out_dir).resolve()
#     out_dir.mkdir(exist_ok=True, parents=True)
#     assert Path(out_dir).exists(), out_dir

#     main(in_dir, ext, out_dir)


# def main(in_dir, ext, out_dir):
#     """Example script."""
#     if not Path(in_dir).exists():
#         print(f"[Error] {in_dir}.")
#         print("File Not Found T.T")
#         print("System shutdown .zzZ")
#         exit()

#     click.echo(banner)
#     click.echo('Hello Ambient!')
#     click.echo('Arthur @peace098beat')
#     click.echo('\n')

#     in_dir = (work_dir / in_dir).resolve()
#     out_dir = (work_dir / out_dir).resolve()

#     click.echo(f'Work_dir Dir:{work_dir}')
#     click.echo(f'Input Dir:{in_dir}')
#     click.echo(f'Output Dir:{out_dir}')
#     click.echo('\n')

#     click.echo(click.style(
#         f'be Transforming... \nPlz take a coffee brake 🧉\n', fg='green'))

#     try:
#         outputs = pipeline.run_dir(in_dir, ext, out_dir)
#     except KeyboardInterrupt:
#         for out_file in outputs:
#             shutil.unlink(out_file)

#     post_process.post_process(out_dir)

#     click.echo(click.style(f'\n\nFin! Check your sounds!  :D\n\n', fg='green'))


@click.command()
@click.argument('in_dir')
@click.argument('ext')
@click.argument('out_dir')
def cli(in_dir, ext, out_dir):
    """Example script."""
    if not Path(in_dir).exists():
        print(f"[Error] {in_dir}.")
        print("File Not Found T.T")
        print("System shutdown .zzZ")
        exit()

    click.echo('Hello Ambient!')

    in_dir = (work_dir / in_dir).resolve()
    out_dir = (work_dir / out_dir).resolve()

    click.echo(f'Work_dir Dir:{work_dir}')
    click.echo(f'Input Dir:{in_dir}')
    click.echo(f'Output Dir:{out_dir}')

    click.echo(f'be Transforming... Plz take a coffee brake 🧉 :D')

    try:
        outputs = pipeline.run_dir(in_dir, ext, out_dir)
    except KeyboardInterrupt:
        for out_file in outputs:
            shutil.unlink(out_file)
    # mono_file, fig_path, json_path, sig_path = outputs

    click.echo(f'Fin! Check your sounds!  :D')
