# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# Kata Author: BattleRattle
# 4 kyu

import itertools

def permutations(s):
    permutations = set(itertools.permutations(sorted(s)))
    permutations = ([''.join(permutation) for permutation in permutations])
    
    return permutations    
    # return ([''.join(permutation) for permutation in set(itertools.permutations(sorted(s)))])


if __name__ == "__main__":
    permutations('a')       #, ['a']);
    permutations('ab')      #, ['ab', 'ba'])
    permutations('aabb')    #, ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
