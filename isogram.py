def is_isogram(string):
    return [True for char in set(string) if string.count(char) > 1]

if __name__ == "__main__":
    is_isogram("aba"), False