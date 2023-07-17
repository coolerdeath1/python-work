from itertools import permutations

letters = ['a', 'e', 'i', 'o', 'I']
perms = permutations(letters)

for p in perms:
    print(''.join(p))