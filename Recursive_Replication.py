@countcalls
def replicate(times, number):
    
    if times < 0 or times == 0:
        return []
    else:
        return [number] + replicate(times-1, number)
    
replicate(3, 5)