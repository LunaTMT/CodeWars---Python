# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/python
# Kata Author: frenetic_be
# 5 kyu

def get_peak(arr, i, j):
    above = arr[i+1]
    middle = arr[i]

    if  above > middle:  
        return get_peak(arr, i+1, 0) #Peaks
    elif above == middle:
        return get_peak(arr, i+1, j-1) #plateau
    elif j:
        return i + j 
    else:
        return i 


def pick_peaks(arr):
    index = []
    i = 0
    
    while True:
        try:
            if arr[i+1] > arr[i]:
                i = (get_peak(arr, i+1, 0))    
                index.append(i)
            else:
                i += 1
        except:
            break
    return {"pos":index, "peaks":[arr[i] for i in index ]}

if __name__ == "__main__":
    pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])       #, {"pos":[3,7], "peaks":[6,3]})
    pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])   #, {"pos":[3,7,10], "peaks":[6,3,2]}
    pick_peaks([2, 1, 3, 1, 2, 2, 2, 2])
