def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
        
def next_bigger(n):
    arr = [*str(n)]
    n = len(arr)

    i = n-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
        
    if i == 0:
        return -1
    
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    
    arr[i-1], arr[j] = arr[j], arr[i-1]
    arr[i:] = reversed(arr[i:])
    
    return int("".join(arr))


next_bigger(2019873457)