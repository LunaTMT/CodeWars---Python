# https://www.codewars.com/kata/529b418d533b76924600085d/solutions/python
# Kata Author: OlgaGr
# 5 kyu

import re

def to_underscore(string):
    try:
        list_ = re.findall('[a-zA-Z][^A-Z]*', string)
        return '_'.join([i.lower() for i in list_])
    except:
        return str(string)
