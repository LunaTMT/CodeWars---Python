def walkee(walk):
    if walk.count('w') - walk.count('e') != 0:
        return False
    elif walk.count('n') - walk.count('s') != 0:
        return False
    else:
        return True
    
    
def is_valid_walk(walk):
    return False if len(walk) != 10 else walkee(walk)