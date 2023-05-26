import math
from collections import defaultdict

class Sudoku(object):
    def __init__(self, data):
        self.data =  data
        
    def is_valid(self):

        hash_ = defaultdict(list)

        n = len(self.data)
        
        """
        when the length of data is:
        25 - sq size = 5
        9  - sq size = 3
        4  - sq size = 2
        We can infer that the square size must be the square root of the length, n.
        """
        square_size = math.sqrt(n) 
        
        for r, row in enumerate(self.data):
            for c, value in enumerate(row):
                if any(isinstance(value, type) for type in (str, bool)) or value == 0: #error checking values
                    return False
                
                #denoting what row, column and square number each value belongs to (respectively) and adding to hash map
                hash_[("r", r)].append(value)
                hash_[("c", c)].append(value)
                hash_[("sq", (r//square_size, c//square_size))].append(value)

        # Each r, c, and sq must add up to the sum from 1 - n 
        # which is this equation
        k = n*(n+1)/2 
        
        for list_ in hash_.values():
            #ensuring the sum of every list is what we expect it to be (i.e. k)
            if (sum(list_) != k): 
                return False
        return True