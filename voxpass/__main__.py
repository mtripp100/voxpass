import click

from .voxpass import generate_password


@click.command()
@click.option(
    "--num-vowels",
    type=click.INT,
    default=3,
    help="Number of vowels in password.",
    show_default=True,
)
def run(num_vowels):
    """Generates passwords in CONSONANT-VOWEL-CONSONANT format for high readability."""
    click.echo(generate_password(num_vowels))


if __name__ == "__main__":
    run()  # pylint: disable=no-value-for-parameter
