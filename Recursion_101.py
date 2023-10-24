def solve(a,b):
    if a==0 or b==0: 
        return [a,b]
    elif a >= 2*b:
        return solve(a % (2*b), b)     
    elif b >= 2*a:
        return solve(a, b % (2*a))
    return [a, b]
        