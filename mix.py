# https://www.codewars.com/kata/5629db57620258aa9d000014/python
# Kata Author: g964
# 4 kyu

import re
import itertools
import operator

def mix(s1, s2):
    chars = set("".join(re.findall(r'[a-z]', s1+s2)))
    counts = sorted([((1, i, s1.count(i)), (2, i, s2.count(i))) for i in chars])
  
    filtered = []
    for x, y in counts:
        
        s_name, char, maximum = x if x[2] > y[2] else y
        IN_BOTH = x[2] == y[2]
        filter = (s_name, char, maximum, IN_BOTH)

        if maximum > 1:
            filtered.append(filter)
      
    filtered = sorted(filtered, key=lambda x: x[2], reverse=True)
    filtered = [list(group) for key,group in itertools.groupby(filtered, operator.itemgetter(2))] #split for number

    final = ""

    for groups in filtered:
        
        groups = sorted(groups, key=lambda x: x[1])
        groups = sorted(groups, key=lambda x: x[0])  

        start = ""
        end = "" 
 
        for group in groups:
            s_name, char, maximum, IN_BOTH = group
            if IN_BOTH:
                end += f"=:{char*maximum}/"
            else: 
                start += f"{s_name}:{char*maximum}/"
        final += start + end
    return final[:-1]
  

if __name__ == "__main__":
    #mix("Are they here", "yes, they are here") #, "2:eeeee/2:yy/=:hh/=:rr"))
    #mix("looping is fun but dangerous", "less dangerous than coding")
    mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") 
    #'2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
