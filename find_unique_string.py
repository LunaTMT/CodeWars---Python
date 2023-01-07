def find_word(letters, lst):
    for i in lst:
        if set(i.lower()) == letters:
            return i


def find_uniq(arr):
    arr2 = list(map(str.lower, arr))
    arr2 = set([''.join(set(i)) for i in (arr2)])
    dict_ = {}
    
    for item in list(arr2):
        try:
            print(item[0])
            count = "".join(arr).count(item[0])
            dict_[item] = (count)
        except:
            pass
           
    letters = set(min(dict_, key=dict_.get))
    return find_word(letters, arr)

if __name__ == "__main__":
    find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])  #, 'BbBb')
    find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])  #, 'foo')
    find_uniq([ '    ', 'a', '  ' ])    #, 'a')
