# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# Kata Author: parceval
# 5kyu


def increment_string(string):
    
    number = ""
    for count, item in enumerate(reversed(string)):
        if item.isnumeric():
            number += item
        else:
            if count > 0:
                string = string[:-count]
            break

    if number:
        numbers = list(number)[::-1]
       # numbers[-1] += 1

        actual_num = []
        for count, item in enumerate(reversed(numbers)):
            if item == '0':
                break
            actual_num.append(int(item) * pow(10, count))
        
        new_num = sum(actual_num) + 1
        diff = len(numbers) - len(str(new_num))


        if numbers == list(string):
            return (diff * '0') + str(new_num)
        return string + (diff * '0') + str(new_num)

    return string + '1'
        





if __name__ == "__main__":
        increment_string("foo") #, "foo1")
        increment_string("foobar001")   #, "foobar002")
        increment_string("foobar1") #, "foobar2")
        increment_string("foobar00")    #, "foobar01")
        increment_string("foobar99")    #, "foobar100")
        increment_string("foobar099")   #, "foobar100")
        increment_string("fo99obar99")  #, "fo99obar100")
