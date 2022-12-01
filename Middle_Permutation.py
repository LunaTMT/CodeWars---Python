#from itertools import permutations
import itertools

def middle_permutation(string):


    permutations = list(itertools.permutations(sorted(string)))
 
    # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    permutations = ([''.join(permutation) for permutation in permutations])
    middleIndex = (len(permutations) - 1)/2
    

    print(permutations[int(middleIndex)])
    return permutations[int(middleIndex)]

if __name__ == "__main__":
        #middle_permutation("abc")       #,"bac")
        #middle_permutation("abcd")      #,"bdca")
        #middle_permutation("abcdx")     #,"cbxda")
        #middle_permutation("abcdxg")    #,"cxgdba")
        #middle_permutation("abcdxgz")   #,"dczxgba")
        middle_permutation("gybpitcfsanwohjvdqlxue")  