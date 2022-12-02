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