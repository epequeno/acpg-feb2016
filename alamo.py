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
@click.option('--name', prompt='your name please')
def goodbye(name):
    click.echo('goodbye {}!'.format(name))


@cli.command()
@click.option('--person', type=(str, int), help='a human being')
def whois(person):
    name = person[0]
    age = person[1]
    click.echo("who: {}\nhow old?: {}".format(name, age))


if __name__ == '__main__':
    cli()