from pathlib import Path
import click
import pipeline

work_dir = Path(".").parent.resolve()

@click.command()
@click.argument('in_file')
def _(in_file):

    """Example script."""
    if not Path(in_file).exists():
        print(f"[Error] {in_file}.")
        print("File Not Found T.T")
        print("System shutdown .zzZ")
        exit()

    click.echo('Hello Ambient!')
    
    click.echo(f'Input Audio File:{in_file}')
    click.echo(f'be Transforming... Plz take a coffee brake :D')
    
    outputs = pipeline.run(in_file=in_file)
    mono_file, fig_path, json_path, sig_path = outputs

    click.echo(f'Fin! Check your sounds! {mono_file} :D')


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
    
    click.echo(f'Input Audio Dir:{work_dir}')
    click.echo(f'Input Audio Dir:{in_dir}')
    click.echo(f'Input Output Dir:{out_dir}')
    click.echo(f'be Transforming... Plz take a coffee brake :D')

    try:
        outputs = pipeline.run_dir(in_dir, ext, out_dir)
    except KeyboardInterrupt:
        for out_file in outputs:
            shutil.unlink(out_file)
    # mono_file, fig_path, json_path, sig_path = outputs

    click.echo(f'Fin! Check your sounds!  :D')

