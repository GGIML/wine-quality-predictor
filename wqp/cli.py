import click
from wqp import __version__
from wqp.workflow import model_training_workflow

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
    model_training_workflow(data_path)