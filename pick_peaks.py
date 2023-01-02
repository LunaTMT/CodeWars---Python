

def is_higher(arr, i, j):
    above = arr[i+1]
    middle = arr[i]

    if  above > middle:
        return is_higher(arr, i+1, 0)
   
    elif above == middle:
        return is_higher(arr, i+1, j-1)
   
    elif j:
        return i + j
    
    else:
        return i


def pick_peaks(arr):

    index = []
    i = 0
    
    while True:
        try:
            middle = arr[i]
            above = arr[i+1]
            if  above > middle:
                i = (is_higher(arr, i+1, 0))
                index.append(i)
            else:
                i += 1
        except:
            break


    print({"pos":index, "peaks":[arr[i] for i in index ]})
    return {"pos":index, "peaks":[arr[i] for i in index ]}



"""

    arr_bool = []
    index = []
    plat = []
    for i, value in enumerate(arr):
        next = arr[i+1]
        below = arr[i-1]

        try:
            if below < value < next:  
                arr_bool.append(True)
     
            
            elif below < value == next:
                arr_bool.append(True)


            else:
                arr_bool.append(False)
                if arr_bool[i-1] == True:
                    index.append(i)
        except:
            arr_bool.append(False)

    print({"pos":index, "peaks":[arr[i] for i in index ]})


    return {"pos":index, "peaks":[arr[i] for i in index ]}
"""

if __name__ == "__main__":
 
    #pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])   #, {"pos":[3,7], "peaks":[6,3]})
    #pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])   #, {"pos":[3,7,10], "peaks":[6,3,2]}
     pick_peaks([2, 1, 3, 1, 2, 2, 2, 2])