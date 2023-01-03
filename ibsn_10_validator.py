def eval_string(idx, value, max_length):
    while True:
        try:
            return eval(f"{idx} * {value}")
        except:
            if value.isalpha():
                if max_length:
                    if value == "X":
                        value = 10
                    else:
                        value = 0
                else:
                    value = 0
            else:
                pass  
            
def valid_ISBN10(isbn): 

    if not isbn or len(isbn) != 10:
        return False
    
    sum_ = sum([eval_string(idx, value, (idx == len(isbn))) for idx, value in enumerate(isbn, start=1)])

    if sum_ != 0:
        return True if sum_ % 11 == 0 else False
    return False