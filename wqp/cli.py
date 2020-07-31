import click
from wqp import __version__

@click.group(name='wqp')
@click.version_option(__version__)
def wqp():
    pass

@wqp.group(name='jobs')
def jobs():
    pass

@jobs.command(name='train')
@click.option('--data-path', '-d')
def train(data_path):
    print(data_path)
    pass