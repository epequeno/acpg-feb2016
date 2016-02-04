intro
-----
- click makes it easy to control the cli stuff independently from the rest of the
application

click in three points
----
- we'll only discuss the first two today

why click
----
- I'm a fan of software with good features "out of the box" and that don't take long to
get the advantage of
- click can a flexible way to configure you application without much thought

the goal
---
- today I'd like to make something that looks like git, the main application
has a set of flags, there are subcommands and those subcommands have flags and
help pages of their own.

## DEMO
- use of decorators
- automatic help page
- docstrings as help page, NOTE: you can't use autodoc/rst/sphinx
- convenience features like echo
- try to run without argument, then with `--help`
=======================
import click


@click.command()
@click.argument('name')
def hello(name):
    """simple program to say hello"""
    click.echo('Hello {}'.format(name))

if __name__ == '__main__':
    hello()
=======================


- options
- types, see what happens with a non INT arg to count
- specifying type or use `default`
=======================
import click


@click.command()
@click.argument('name')
@click.option('-c', '--count') # default=1 / type=click.INT here
def hello(name, count):
    """simple program to say hello"""
    for i in range(count):
        click.echo('Hello {}'.format(name))

if __name__ == '__main__':
    hello()
=======================


- subcommands
- we added the click.group() which acts as a 'wrapper' around the whole cli application
- we can then add commands in 'groups' with options, arguments etc along with the definition
of the code that controls the function
- notice that we went from using `click.command()` to `cli.command()` which specifies the
group the command belongs to.
=======================
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.option('-c', '--count', default=1)
def hello(name, count):
    """simple program to say hello"""
    for i in range(count):
        click.echo('Hello {}'.format(name))


@cli.command()
def goodbye():
    click.echo('goodbye!')

if __name__ == '__main__':
    cli()
=======================


- let's move the business logic out of alamo.py and into another package
- now alamo.py is only asking another package to compute an answer, now we're only
looking at the overall structure of the application, not the implementation of the
solution.
- I've created the package `utils` to transform the name and return back to me
what I should display
=======================
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
=======================
