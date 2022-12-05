def move_zeros(arr):

    l = [i for i in arr if i!=0]    
    return l+[0]*(len(arr)-len(l)) 

    for i in range(0, len(lst)):
        if lst[i] == 0:
            item = lst[i]
            lst.remove(item)
            lst.insert(len(lst), item)
    return lst


if __name__ == "__main__":
    move_zeros([1, 0, 1, 2, 0, 1, 3])