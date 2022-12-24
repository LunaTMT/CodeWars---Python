def descending_order(num):
    arr = list(map(str, str(num)))
    arr.sort(reverse=True)
    return int("".join(arr))

if __name__ == "__main__":
    descending_order(123456789)
