def alphabet_position(text):
    alphabet = list(map(chr, range(97, 123)))
    dict_ = {letter: str(i+1) for i, letter in enumerate(alphabet)} 
    text = list(map(lambda x: dict_[x] if x in dict_ else False, text.lower()))
    
    return " ".join(list(filter(bool, text)))
    