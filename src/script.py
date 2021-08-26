from pathlib import Path
import click
import pipeline

@click.command()
@click.argument('in_file')
def cli(in_file):

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

