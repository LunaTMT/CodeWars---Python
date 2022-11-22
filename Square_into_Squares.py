#https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python
# kata author: g964
# Uncompleted kata - Does not have backtracking implemented·

import math

def check_increasing(array):
    if len(array) > len(set(array)):
        return None
    return array

def decompose(n):
    answer = [n-1]
    quotient = n**2 - (n-1)**2

    #Dividend / Divisor  = Quotient with Remainder

    while quotient >= 1:
        sqr_rt = int(math.sqrt(quotient))
        answer.append(sqr_rt)
        quotient = quotient - sqr_rt**2 
    
    if quotient == 1:
        answer.append(1)

    return check_increasing(answer[::-1])

if __name__ == "__main__":
    #decompose(30)
    #decompose(5)    #, [3,4])
    decompose(2256307)
    decompose(8)    #, None)
