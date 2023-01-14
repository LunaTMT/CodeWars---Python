# https://www.codewars.com/kata/5b752a42b11814b09c00005d/train/python
# Kata Author: KenKamau
# 7 kyu

def solve(a,b):
    if a == 0 or b == 0:
        return [a,b] 
    elif a >= (2*b):
        return solve(a - (2*b), b)
    elif b >= (2*a):
        return solve(a, b - (2*a))
    else:
         return [a,b] 
    
if __name__ == "__main__":
    solve(6,19) #,[6,7]
