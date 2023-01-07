# https://www.codewars.com/kata/546f922b54af40e1e90001da/solutions/python
# Kata Author: MysteriousMagenta
# 6 kyu

def alphabet_position(text):
    alphabet = list(map(chr, range(97, 123)))
    dict_ = {letter: str(i+1) for i, letter in enumerate(alphabet)} 
    text = list(map(lambda x: dict_[x] if x in dict_ else False, text.lower()))
    
    return " ".join(list(filter(bool, text)))
    
