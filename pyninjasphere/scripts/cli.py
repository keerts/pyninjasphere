# Skeleton of a CLI
"""
Ninjasphere cli
"""

import click

from pyninjasphere.logic.node import Node


@click.group()
def cli():
    """ I pass on this one """
    pass


@cli.command()
@click.option('--host', default="ninjasphere.local")
def list(host):
    """ list the things from a node """
    click.echo("listing things from host %s" % host)
    node = Node(host)
    click.echo(node.get_all_things())
