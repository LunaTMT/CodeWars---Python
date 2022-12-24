def find_it(seq):
    answer = list(map(lambda x: x if seq.count(x) % 2 > 0 else None, set(seq)))
    value = [val for val in answer if val != None]
    return int(value[0])


if __name__ == "__main__":
    find_it([1,1,1,1,1,1,10,1,1,1,1])   #, 10);