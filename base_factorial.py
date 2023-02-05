import string as st
import math
def dec_2_fact_string(nb):
    d = dict(zip([i for i in range(0, 37)], [str(i) for i in range(0,10)] + list(st.ascii_uppercase)))

    
    base = []
    Quotient = nb
    i = 1
    while Quotient != 0:
        remainder = Quotient % i
        base.append(d[int(remainder)])
        Quotient //= i
        i += 1
        
    return ''.join(base)


def fact_string_2_dec(string):
    d = dict(zip([str(i) for i in range(0,10)] + list(st.ascii_uppercase), [i for i in range(0, 37)]))
    print(d)
    amount = 0
    for idx, char in enumerate(string[::-1]):
        amount +=  d[char] * math.factorial(idx)
    
    return amount
if __name__ == "__main__":
    dec_2_fact_string(371993326789901217467999448150835199999999)  
    # #, "ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210'") 

    fact_string_2_dec("341010")  #, 463)