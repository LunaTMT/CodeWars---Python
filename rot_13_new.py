# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/python
# Kata Author: hvaara
# 5 kyu

def get_chr(i):
    unicode_val = ord(i)
    rot_13 = unicode_val + 13

    if unicode_val < 65 or (91 <= unicode_val <= 96) or unicode_val > 122:
        return i

    elif i == i.upper():
        if rot_13 > 90:
            return chr((rot_13 % 90) + 64)
        else:
            return chr(rot_13)

    elif i == i.lower():
        if rot_13 > 122:
            return chr((rot_13 % 122) + 96)
        else:
            return chr(rot_13)
    else:
        return i


def rot13(message):
    return "".join([get_chr(i) for i in message])




if __name__ == "__main__":
    #rot13(" rknzcyr.") #, "ROT13 example.")
    rot13("@[`{")   #, "@[`{")
