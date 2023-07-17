#Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
from itertools import permutations

letters = ['a', 'e', 'i', 'o', 'I']
perms = permutations(letters)

for p in perms:
    print(''.join(p))