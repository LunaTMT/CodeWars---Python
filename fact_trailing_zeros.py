import math

def zeros(n):
    
    if n == 0:
        return 0
    
    sum = 0
    for k in range(1, int(math.log(n,5) + 1)):
           sum += int(abs(n/pow(5,k)))     
    return sum

if __name__ == "__main__":
    zeros(30) #7