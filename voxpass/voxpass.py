#!/usr/bin/python3

import string
import math
import random
import sys


vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in list(string.ascii_lowercase) if x not in vowels]
crypto = random.SystemRandom()

def genpass(num_vowels, allow_dups):	
	letters = gen_with_dups(num_vowels) if allow_dups else gen_without_dups(num_vowels)
	return ''.join(letters)

def gen_with_dups(num_vowels):
	return [crypto.choice(vowels if x % 3 == 1 else consonants) for x in range(num_vowels * 3)]

def gen_without_dups(num_vowels):
	sampled_vowels = crypto.sample(vowels, num_vowels)
	sampled_consonants = crypto.sample(consonants, num_vowels * 2)
	
	return [sampled_vowels.pop() if x % 3 == 1 else sampled_consonants.pop() for x in range(num_vowels * 3)]

if __name__ == '__main__':
	print(genpass(int(sys.argv[1]), True))
	print(genpass(int(sys.argv[1]), False))
