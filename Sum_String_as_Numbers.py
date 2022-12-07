# https://www.codewars.com/kata/5324945e2ece5e1f32000370/solutions
# Kata Author: nicknovitski
# 4 Kyu
# Not completed: Does not work for float(inf) values - exe timeout

def sum_strings(x, y):

    if x and y:
        return str(int(x) + int(y))
    elif x and not y:
        return x
    elif not x and y:       
        return y
    elif not x and not y:        
        return '0'      
    else:
        return str(int(float(x)) + int(float(y)))


if __name__ == "__main__":
    sum_strings("1", "1")       #, "2")
    sum_strings("123", "456")   #, "579")
