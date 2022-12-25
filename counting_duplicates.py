# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/
# Kata Author: kgashok
# 6 Kyu

def duplicate_count(text):
    check = list(map(lambda x: True if text.count(x) > 1 else False, [x for x in set(text.lower())]))

    
if __name__== "__main__":
    duplicate_count("Indivisibilities")
