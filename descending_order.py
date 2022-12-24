# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
# Kata Author: TastyOs
# 7 Kyu

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

if __name__ == "__main__":
    descending_order(123456789)
