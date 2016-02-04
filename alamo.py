import click

# local
import utils


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.option('-c', '--count', default=1)
def hello(name, count):
    """simple program to say hello"""
    click.echo(utils.say_hello(name, count))


@cli.command()
def goodbye():
    click.echo('goodbye!')

if __name__ == '__main__':
    cli()