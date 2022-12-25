def duplicate_count(text):
    check = list(map(lambda x: True if text.count(x) > 1 else False, [x for x in set(text.lower())]))
    print()
if __name__== "__main__":
    duplicate_count("Indivisibilities")
