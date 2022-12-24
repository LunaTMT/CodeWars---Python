
def array_diff(a, b):

    new_list =  list(filter(lambda x: (x not in b), a))


    print(list(filter(bool, new_list)))
    return list(filter(bool, new_list))

if __name__ == "__main__":
    array_diff([1, 2, 2], [2])
    array_diff([1,2,3], [1, 2]) #, [3],