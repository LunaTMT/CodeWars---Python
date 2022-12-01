# https://www.codewars.com/kata/58ad317d1541651a740000c5/solutions
# Could not finish due to optimisation constrain on kata
# Kata Author: myjinxin2015 
# 4 kyu

import itertools

def middle_permutation(string):
    permutations = list(itertools.permutations(sorted(string)))
    permutations = ([''.join(permutation) for permutation in permutations])
    middleIndex = (len(permutations) - 1)/2
    
    return permutations[int(middleIndex)]

if __name__ == "__main__":
        middle_permutation("abc")       #,"bac")
        middle_permutation("abcd")      #,"bdca")
        middle_permutation("abcdx")     #,"cbxda")
        middle_permutation("abcdxg")    #,"cxgdba")
        middle_permutation("abcdxgz")   #,"dczxgba")
        middle_permutation("gybpitcfsanwohjvdqlxue")  #Not optimised to handle <---
