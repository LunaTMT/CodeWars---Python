# completed kata but does not meet the requirement for efficiency.
# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
# Kata Author: raulbc777
# 4 kyu

def find_all(sum_dig, digs):
    valid = []

    for i in range(int("9" * (digs-1)) + 1, int("9"*digs) + 1):
        split = [int(x) for x in str(i)]
        
        if sum(split) == sum_dig and sorted(split) == split:
                valid.append(i)

    if not valid:
        return []
    return [len(valid), valid[0], valid[-1]]



if __name__ == "__main__":
    find_all(10, 3) #, [8, 118, 334])
    find_all(27, 3) #, [1, 999, 999])
    find_all(84, 4) #, [])
    find_all(35, 6) #, [123, 116999, 566666])



    
"""
#TOP

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]
"""
