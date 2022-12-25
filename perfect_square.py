def is_square(n): 
    if n == 0:
        return True
    if n < 0:
        return False

    ps = []

    for count in range(1, n):
        if pow(count, 2) > n:
            break
        ps.append(True) if pow(count, 2) == n else False
    
    return True if ps else False
    


if __name__ == "__main__":
    is_square(1990765924)
