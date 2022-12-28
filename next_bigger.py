from itertools import permutations

def next_bigger(n):
    comb =  sorted(set(permutations((map(int, str(n))))))
    n = tuple(map(int , str(n)))
    index = comb.index(n)
    
    try:
        return  int(''.join(map(str,comb[index + 1])))
    except:
        return -1


if __name__ == "__main__":
    next_bigger(4561456875334567)   