#!/usr/bin/env python3

import string
import random
import click

VOWELS = ('a', 'e', 'i', 'o', 'u')
CONSONANTS = tuple(x for x in string.ascii_lowercase if x not in VOWELS)


@click.command()
@click.option('--num-vowels', type=click.INT, default=3, help='Number of vowels in password.', show_default=True)
def genpass(num_vowels):
    """Generates passwords in CONSONANT-VOWEL-CONSONANT format for high readability."""
    rand = random.SystemRandom()
    letters = (rand.choice(VOWELS if x % 3 == 1 else CONSONANTS) for x in range(num_vowels * 3))
    click.echo(''.join(letters))


if __name__ == '__main__':
    genpass()  # pylint: disable=E1120
