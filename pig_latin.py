# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# Kata Author: user2505876
# 5 kyu

def pig_it(text):
    words = text.split()
    return " ".join(list(map(pig_latin, words)))

def pig_latin(n):
    if n.isalnum():
        return n[1:] + n[0] + "ay" 
    return n
  

if __name__ == "__main__":
    pig_it('Pig latin is cool') #,'igPay atinlay siay oolcay')
