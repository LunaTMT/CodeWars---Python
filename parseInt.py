#Please note this is not my code:
# author of code: recursive
# https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers


import re

def parse_int(textnum, numwords={}):
    if not numwords:
      
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

     #create dictionary numwords
      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = re.split(' |\-', textnum)
    

    current = result = 0
    for word in textnum:
        
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]   
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    print(result + current)
    return result + current


if __name__ == "__main__":
    parse_int('one')    #, 1)
    parse_int('twenty') #, 20)
    parse_int('two hundred forty-six')  #, 246)
    parse_int('one thousand two hundred forty-six')  #, 1246)
    parse_int('seven hundred eighty-three thousand nine hundred and nineteen')  # 783919
