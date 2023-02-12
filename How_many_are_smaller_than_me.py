def smaller(arr):
    return [sum([1 for i in arr[idx:] if i < value]) for idx, value in enumerate(arr)]