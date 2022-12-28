# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
# Kata Author: GiacomoSorbi
# 4 kyu

#Unfinished kata, works but but not optimised.


from itertools import permutations

def next_bigger(n):
    comb =  sorted(set(permutations((map(int, str(n))))))
    n = tuple(map(int , str(n)))
    index = comb.index(n)
    
    try:
        return int(''.join(map(str,comb[index + 1])))
    except:
        return -1


if __name__ == "__main__":
    next_bigger(4561456875334567)   
