def printXY(x, y):
    print("X: ", x)
    print("Y: ", y)


def sum_strings(x, y):
    print()
    
    if x and y:
        print("C1")
        printXY(x, y)
        return str(int(float(x)) + int(float(y)))
    
    elif not x and not y:        
        print("C2")
        printXY(x, y)
        return '0'
    
    elif not x and y:       
        print("C3")
        printXY(x, y)
        return y
    
    elif x and not y:
        print("C4")
        printXY(x, y)
        return x

if __name__ == "__main__":
    sum_strings(9999999999999999, 1)
