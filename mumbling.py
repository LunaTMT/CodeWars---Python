def accum(s):
    string  = ""
    for count, value in enumerate(s, start=1):
        string += (value.upper()) + (value.lower() * (count-1) + "-")
    return string[:-1]
    

if __name__ == "__main__":
    accum("ZpglnRxqenU"), 
    #"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")