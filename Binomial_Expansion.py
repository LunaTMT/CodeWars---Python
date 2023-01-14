import math
import re

def expand(expr):
    brackets = (expr[expr.find("(")+1:expr.find(")")])
    
    for i, value in enumerate(brackets):
        if value == "-" or value == "+" and i != 0:
            a = brackets[0:i]
            b = brackets[i:]
    
    a_num, a_letter = get_num_letter(a)

    pow = [*expr][-1]
    if pow == '0':
        return '1'
    elif pow == '1':
        return a + b

    
    co_dict = {         '2' :       [1, 2, 1],
                        '3' :     [1, 3, 3, 1],
                        '4' :   [1, 4, 6, 4, 1],
                        '5' : [1, 5, 10, 10, 5, 1],
                   }

    expansion = []
    coeff = co_dict[pow]

    pow = int(pow)
    b = int(b)
    
    for i, value in enumerate(coeff):
        if i == 0:
            expansion.append(f"{a_num ** pow if not (-1 <= a_num <= 1)   else ''}{a_letter}^{pow}")
            
        elif i == len(coeff) - 1:
            expansion.append(f"{get_power(b, pow)}")
                   
        else: 
            a_pow = (len(coeff) - 1) - i
            b_pow = i
            expansion.append(
            f'{value * (a_num ** a_pow if a_num else 1) * (b ** b_pow if b else 1)}'
            f'{a_letter}'
            f'{("^" + str(pow-i)) if (pow-i > 1) else ""}'
            )

    
    expansion = ["+" + value  if "-" not in value else value  for i, value in enumerate(expansion[1:], start=1)]

    return "".join(expansion)

    

def get_num_letter(x):
    split = re.split('(\d+)',x)

    num = "".join(split[:-1])
    letter = split[-1]

    try: 
        num = int(num)
    except:
        pass
    
    if letter[0] == '-':
        num = -1
        letter = letter[-1]

    if num == '':
        num = 0

    return (num, letter)

def get_power(x, p):
    eval = int(math.pow(x, int(p)))
    return eval if abs(eval) >= 1 else "1"



if __name__ == "__main__":
    expand("(-r+8)^4") #' r^4 - 32r^3 + 384r^2 - 2048r + 4096'