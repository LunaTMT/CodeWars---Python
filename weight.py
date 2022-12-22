# kata: https://www.codewars.com/kata/55c6126177c9441a570000cc
# kata author: g964
# 5 kyu

def order_weight(string):
    #spliting string into elements
    # "103 123 4444 99 2000" -> ['2000', '10003', '1234000', '44444444', '9999', '11', '11', '22', '123']
    values = string.split(' ') 
    
    #splitting each value in the string into its own list and summing it
    weights =  [sum([int(x) for x in value]) for value in values] 

    #sorting by weights 
    weights, values = zip(*sorted(zip(weights, values)))
    return " ".join(values)



if __name__ == "__main__":
    order_weight("103 123 4444 99 2000")
    #"11 11 2000 10003 22 123 1234000 44444444 9999")
