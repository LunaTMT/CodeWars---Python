import re

def to_underscore(string):
    try:
        list_ = re.findall('[a-zA-Z][^A-Z]*', string)
        return '_'.join([i.lower() for i in list_])
    except:
        return str(string)