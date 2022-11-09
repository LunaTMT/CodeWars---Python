import primefac



def sum_for_list(lst):
    

    #finds prime factors for each element 'i' of list and creates 2d list with according prime factors attached
    index = 0
    unique_factors = []
    for i in lst:

        factors = list( primefac.primefac(i) )        
        lst.pop(index)
        lst.insert(index, [i, factors]) #removes and adds new element with its coresponding factors
        index += 1
        
        #saves all factors
        unique_factors.append(' '.join(str(x) for x in factors))

    unique_factors = set(list(map(int, (' '.join(unique_factors).split())))) #excludes all but unique factors


    #checking IF unique factor (i) exists in initial value's prime factors (j[1])  
    # TRUE --> y = sum of initial values 
    final = []    

    for i in unique_factors:
        y = 0
        for j in lst:
            if i in j[1]:
                y += j[0] 
        final.append([i, y])
   
    print(final)
    return(final)

if __name__ == "__main__":
    sum_for_list([12, 15]) #[[2, 12], [3, 27], [5, 15]])
    sum_for_list([15, 21, 24, 30, 45]) #[[2, 54], [3, 135], [5, 90], [7, 21]]








# author - g964 - https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python