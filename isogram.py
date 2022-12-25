# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Kata Author: chunjef
# 7 kyu

def is_isogram(string):
    string = string.lower()
    if len([True for char in set(string) if string.count(char) > 1]) >= 1:
        return False
    return True

if __name__ == "__main__":
    is_isogram("aba"), False
