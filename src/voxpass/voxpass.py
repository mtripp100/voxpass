import random
import string

VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = tuple(x for x in string.ascii_lowercase if x not in VOWELS)


def generate_password(num_vowels):
    rand = random.SystemRandom()
    letters = (
        rand.choice(VOWELS if x % 3 == 1 else CONSONANTS) for x in range(num_vowels * 3)
    )
    return "".join(letters)
