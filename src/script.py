
from pathlib import Path
import click
import pipeline


def test_run():

	in_file = "./data/1_bouba_woman.wav"
	out_dir = "./outputs/"
	out_file = Path(out_dir) / Path(in_file).name

	assert Path(in_file).exists()

	pipeline.run(in_file=in_file, out_dir=out_dir)

	assert Path(out_dir).exists()
	assert Path(out_file).exists()



@click.command()
@click.argument('infile')
# @click.option('--infile', '-i', help='Input audio file')
def cli(infile):
    """Example script."""
    click.echo('Hello Ambient!')
    click.echo(f'Input Audio File:{infile}')
