#!/usr/bin/python3

import string
import random
import click


vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in list(string.ascii_lowercase) if x not in vowels]
crypto = random.SystemRandom()

@click.command()
@click.option('--num_vowels', type=click.INT, default=3, help='Number of vowels in password (default = 3).')
@click.option('--allow-dups', is_flag=True, help='Allow duplicate letters in password.')
def genpass(num_vowels, allow_dups):
    """Generates passwords in CONSONANT-VOWEL-CONSONANT format for high readability."""
    letters = gen_with_dups(num_vowels) if allow_dups else gen_without_dups(num_vowels)
    click.echo(''.join(letters))

def gen_with_dups(num_vowels):
    return [crypto.choice(vowels if x % 3 == 1 else consonants) for x in range(num_vowels * 3)]

def gen_without_dups(num_vowels):
    sampled_vowels = crypto.sample(vowels, num_vowels)
    sampled_consonants = crypto.sample(consonants, num_vowels * 2)

    return [sampled_vowels.pop() if x % 3 == 1 else sampled_consonants.pop() for x in range(num_vowels * 3)]

if __name__ == '__main__':
    genpass()
