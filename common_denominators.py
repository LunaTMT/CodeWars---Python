import numpy as np
from math import gcd

def convert_fracts(lst):
    print(lst)
    
    if lst:
        lst = np.array(lst)
        
        bot = lst[:, 1]

        cm_den = 1
        for i in bot:
            cm_den = cm_den*i//gcd(cm_den, i)

        mult = [cm_den/i for i in bot]
        top = lst[:, 0] * mult
        
        return list(map(list, (zip(top ,[cm_den] * len(top)))))
    else:
        return []

if __name__ == "__main__":
    convert_fracts([[27115, 5262], [87546, 11111111], [43216, 255689]])

