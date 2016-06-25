""" Ninjasphere cli """

import click

from pyninjasphere.services.service import Service

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

DEFAULT_HOST = "ninjasphere.local"
DEFAULT_MQTT_PORT = 1883
DEFAULT_REST_PORT = 8000

SHORT_HELP_LIST_THINGS = "List the things attached to the Ninja Sphere."
SHORT_HELP_GET_JSON = "Get the json code of the things attached to " \
                      "the Ninja Sphere."
SHORT_HELP_PUBLISH = "Publish a message to the Ninja Sphere's mqtt."
SHORT_HELP_SUBSCRIBE = "Subscribe to the Ninja Sphere's mqtt " \
                       "to get all messages published to a given topic in it."

HELP_HOST = "The host address of the Ninja Sphere."
HELP_MQTT_PORT = "The port of the mqtt of the Ninja Sphere."
HELP_REST_PORT = "The port of the rest server."
HELP_URL = "The url you want to retrieve the json code from."
HELP_TOPIC = "The topic you want to publish data to."
HELP_PAYLOAD = "The data you want to publish to the topic."

METAVAR_COMMAND = "<options>"
METAVAR_HOST = "<ip>"
METAVAR_INT = "<number>"
METAVAR_URL = "<url>"
METAVAR_TOPIC = "<name>"

SHORT_ARGUMENT_HOST = "-h"
SHORT_ARGUMENT_MQTT_PORT = "-m"
SHORT_ARGUMENT_REST_PORT = "-r"
SHORT_ARGUMENT_URL = "-u"
SHORT_ARGUMENT_TOPIC = "-t"
SHORT_ARGUMENT_PAYLOAD = "-p"

LONG_ARGUMENT_HOST = "--host"
LONG_ARGUMENT_MQTT_PORT = "--mqtt-port"
LONG_ARGUMENT_REST_PORT = "--rest-port"
LONG_ARGUMENT_URL = "--url"
LONG_ARGUMENT_TOPIC = "--topic"
LONG_ARGUMENT_PAYLOAD = "--payload"


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Call the things service on the Ninja Sphere.
    """

    pass


@cli.command(options_metavar=METAVAR_COMMAND,
             short_help=SHORT_HELP_LIST_THINGS)
@click.option(SHORT_ARGUMENT_HOST, LONG_ARGUMENT_HOST,
              metavar=METAVAR_HOST, default=DEFAULT_HOST,
              help=HELP_HOST)
@click.option(SHORT_ARGUMENT_MQTT_PORT, LONG_ARGUMENT_MQTT_PORT,
              metavar=METAVAR_INT, default=DEFAULT_MQTT_PORT,
              help=HELP_MQTT_PORT)
@click.option(SHORT_ARGUMENT_REST_PORT, LONG_ARGUMENT_REST_PORT,
              metavar=METAVAR_INT, default=DEFAULT_REST_PORT,
              help=HELP_REST_PORT)
def list(host, mqtt_port, rest_port):
    """
    List the things registered with the Ninja Sphere.

    :param host: Host address of the Ninja Sphere.
    :param mqtt_port: Port of the mqtt server of the Ninja Sphere.
    :param rest_port: Port of the rest interface.
    """

    click.echo("Listing things from host " + host + ".")
    service = Service(host, mqtt_port, str(rest_port))
    things = service.get_all_things()
    for thing in things:
        click.echo(thing.__dict__)
    if len(things) == 0:
        click.secho("Unable to retrieve any things!", fg="red", bold=True)


@cli.command(options_metavar=METAVAR_COMMAND,
             short_help=SHORT_HELP_GET_JSON)
@click.option(SHORT_ARGUMENT_HOST, LONG_ARGUMENT_HOST,
              metavar=METAVAR_HOST, default=DEFAULT_HOST,
              help=HELP_HOST)
@click.option(SHORT_ARGUMENT_MQTT_PORT, LONG_ARGUMENT_MQTT_PORT,
              metavar=METAVAR_INT, default=DEFAULT_MQTT_PORT,
              help=HELP_MQTT_PORT)
@click.option(SHORT_ARGUMENT_REST_PORT, LONG_ARGUMENT_REST_PORT,
              metavar=METAVAR_INT, default=DEFAULT_REST_PORT,
              help=HELP_REST_PORT)
@click.option(SHORT_ARGUMENT_URL, LONG_ARGUMENT_URL,
              metavar=METAVAR_URL, help=HELP_URL)
def get_json(host, mqtt_port, rest_port, url):
    """
    Get the json code of the things attached to the Ninja Sphere.

    \b
    :param host: Host address of the Ninja Sphere.
    :param mqtt_port: Port of the mqtt server of the Ninja Sphere.
    :param rest_port: Port of the rest interface.
    :param url: Url you want to retrieve the json code from.
    """

    if url is None:
        url = "http://" + host + ":" + str(rest_port) + \
              "/rest/v1/things"
    click.echo("Getting json code from url " + url + ".")
    service = Service(host, mqtt_port, rest_port)
    json_code = service.get_data_with_http(url)
    if json_code is not None:
        click.secho("Successfully retrieved the json code!", fg="green",
                    bold=True)
        click.echo(json_code)
    else:
        click.secho("There was an error retrieving the json code!",
                    fg="red", bold=True)


@cli.command(options_metavar=METAVAR_COMMAND,
             short_help=SHORT_HELP_PUBLISH)
@click.option(SHORT_ARGUMENT_HOST, LONG_ARGUMENT_HOST,
              metavar=METAVAR_HOST, default=DEFAULT_HOST,
              help=HELP_HOST)
@click.option(SHORT_ARGUMENT_MQTT_PORT, LONG_ARGUMENT_MQTT_PORT,
              metavar=METAVAR_INT, default=DEFAULT_MQTT_PORT,
              help=HELP_MQTT_PORT)
@click.option(SHORT_ARGUMENT_REST_PORT, LONG_ARGUMENT_REST_PORT,
              metavar=METAVAR_INT, default=DEFAULT_REST_PORT,
              help=HELP_REST_PORT)
@click.option(SHORT_ARGUMENT_TOPIC, LONG_ARGUMENT_TOPIC,
              metavar='<name>', help=HELP_TOPIC, prompt=True)
@click.option('-p', '--payload', metavar='<string>',
              help=HELP_PAYLOAD, prompt=True)
def publish(host, mqtt_port, rest_port, topic, payload):
    """
    Publish a message to the Ninja Sphere's mqtt.

    \b
    :param host: Host address of the Ninja Sphere.
    :param mqtt_port: Port of the mqtt server of the Ninja Sphere.
    :param rest_port: Port of the rest interface.
    :param topic: Topic you want to publish data to.
    :param payload: Data you want to publish to the topic.
    """

    click.echo("Publishing the following message: " + payload + ".")
    service = Service(host, mqtt_port, rest_port)
    if service.mqtt_client.is_connected:
        if service.publish(topic, payload):
            click.secho("Message successfully published on topic: " + topic +
                        ".", fg="green", bold=True)
        else:
            click.secho("There was an error publishing this message!",
                        fg="red", bold=True)
    else:
        click.secho("The client was unable to connect to the mqtt broker!",
                    fg="red", bold=True)


@cli.command(options_metavar=METAVAR_COMMAND,
             short_help=SHORT_HELP_SUBSCRIBE)
@click.option(SHORT_ARGUMENT_HOST, LONG_ARGUMENT_HOST,
              metavar=METAVAR_HOST, default=DEFAULT_HOST,
              help=HELP_HOST)
@click.option(SHORT_ARGUMENT_MQTT_PORT, LONG_ARGUMENT_MQTT_PORT,
              metavar=METAVAR_INT, default=DEFAULT_MQTT_PORT,
              help=HELP_MQTT_PORT)
@click.option(SHORT_ARGUMENT_REST_PORT, LONG_ARGUMENT_REST_PORT,
              metavar=METAVAR_INT, default=DEFAULT_REST_PORT,
              help=HELP_REST_PORT)
@click.option(SHORT_ARGUMENT_TOPIC, LONG_ARGUMENT_TOPIC,
              metavar=METAVAR_TOPIC, help=HELP_TOPIC, prompt=True)
def subscribe(host, mqtt_port, rest_port, topic):
    """
    Subscribe to the Ninja Sphere's mqtt to get all
    messages published to a given topic in it.

    \b
    :param host: Host address of the Ninja Sphere.
    :param mqtt_port: Port of the mqtt server of the Ninja Sphere.
    :param rest_port: Port of the rest interface.
    :param topic: Topic you want to subscribe to.
    """
    click.echo("Subscribing to topic: " + topic + ".")
    service = Service(host, mqtt_port, rest_port)
    if service.mqtt_client.is_connected:
        if not service.subscribe(topic):
            click.secho("There was an error subscribing to this topic!",
                        fg="red", bold=True)
    else:
        click.secho("The client was unable to connect to the mqtt broker!",
                    fg="red", bold=True)
