def all_permuted(n):
    
    def recursion(n):
        if n == 0:
            return 1
        elif n > 0: 
            return n * (recursion(n-1)) + (-1)**n
        
    return recursion(n)