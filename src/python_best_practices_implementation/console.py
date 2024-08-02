import textwrap
import locale

import click
import requests

from . import __version__


API_URL = f"https://{locale.getlocale()[0].split('_')[0]}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()

        title = data["title"]
        extract = data["extract"]

        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract)) 

    except requests.exceptions.ConnectionError:
        click.secho("Unknown locale", fg="red")
