def rot13(message):


    alphabet = list(map(chr, range(97, 123)))
    shifted = list(map(chr, range(110, 123))) + list(map(chr, range(97, 110)))
    dict_ = {alphabet[i]: shifted[i] for i in range(len(alphabet))}


    cap = [] #Boolean list - Determines capital letter index
    
    for i in range(0, len(message)):
        if message[i].isupper():
            cap.append(True)
        cap.append(False)
    
    
    letters = list(message.lower())
    output = [dict_[char] for char in letters]


    for i in range(0, len(cap)):
        if cap[i]:
            output[i] = output[i].upper()
    return output

if __name__ == "__main__":
   # rot13('test')
    rot13('Test')
    #rot13('aA bB zZ 1234 *!?%')



