import pandas as pd

def is_prime(num): 
    for x in range(2, num):
        if num % x == 0: #If there is any number divisible between 2, n-1 --> not prime (1 & n are always factors)
            return False
    return True, 

def prime_factors(n):

    if is_prime(n):
        return f"({n})"

    nums = range(2, 1000)
    prime_numbers = list(filter(is_prime, nums))

    factors=  []

    while n not in prime_numbers:
        for x in prime_numbers:
            if n % x == 0: #is a factor
                factors.append(x)
                n /= x
                break
            else:
                pass
    factors.append(int(n))


    dict = (pd.Series(factors).value_counts(sort=False)).to_dict() #frequency count 
    output = ""

    for key in dict:
        value = dict[key]
        if value > 1:
            output += f"({key}**{value})"
        else:
            output += f"({key})"
    return output

if __name__ == "__main__":
  #  prime_factors(60)
   #  prime_factors(7775460)      #, "(2**2)(3**3)(5)(7)(11**2)(17)")
     prime_factors(18195729)#        , "(7919)")