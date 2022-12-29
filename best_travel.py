
from itertools import combinations

def choose_best_sum(t, k, ls):
    valids = []

    for value in list(combinations(ls, k)):
        if(sum(value)) <= t:
            valids.append(sum(value))

    print(valids)


if __name__ == "__main__":

    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    choose_best_sum(230, 4, xs)    #, 230)
    choose_best_sum(430, 5, xs) #, 430)
    choose_best_sum(430, 8, xs) #, None)
