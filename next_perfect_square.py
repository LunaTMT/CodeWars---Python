import math
def find_next_square(sq):
    n = math.pow(math.sqrt(sq) + 1, 2) 
    return n if not n != int(n) else -1
