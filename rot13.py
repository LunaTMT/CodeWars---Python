# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# Kata author: Rubikan
# 5 kyu

def rot13(message):
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.!@#$%^&*+?~()_-+=:;<>'
    shifted = ' NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890.!@#$%^&*+?~()_-+=:;<>'
    dict_ = {[*alphabet][i]: [*shifted][i] for i in range(len(alphabet))}
    return "".join([dict_[char] for char in list(message)])

if __name__ == "__main__":
    rot13("Test")
    rot13('aA bB zZ 1234 *!?%')
