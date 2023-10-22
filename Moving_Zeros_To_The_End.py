def move_zeros(arr):
    res = [i for i in arr if i != 0]
    return res + [0] * arr.count(0)