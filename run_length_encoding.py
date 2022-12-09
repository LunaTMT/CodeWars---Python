def run_length_encoding(message):
    RLE = []
    i = 0
 
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        RLE.append([count, ch])
        i = j+1

    return RLE


if __name__ == "__main__":
    run_length_encoding("ABBBBCCCCCCCCAB")
