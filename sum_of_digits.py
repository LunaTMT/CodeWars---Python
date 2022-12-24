def recusive_func(value):
    value = sum(value)
    if len(str(value)) >= 2:
        return recusive_func(list(map(int, str(value))))
    return False, value


def digital_root(n):
    _ = True
    while _:
        _, n = recusive_func(list(map(int, str(n))))
    print()
    return n
    

if __name__ == "__main__":
    digital_root(493193)#, 2)