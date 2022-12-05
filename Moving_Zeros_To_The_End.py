# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# kata author: xcthulhu
# 5kyu

def move_zeros(lst):

    for i in range(0, len(lst)):
        if lst[i] == 0:
            item = lst[i]
            lst.remove(item)
            lst.insert(len(lst), item)
    return lst

if __name__ == "__main__":
    move_zeros([1, 0, 1, 2, 0, 1, 3])
    
    
    
#   l = [i for i in arr if i!=0]   
#   return l+[0]*(len(arr)-len(l))    
