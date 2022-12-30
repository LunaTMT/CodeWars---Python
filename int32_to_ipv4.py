def int32_to_ip(int32):
    bin_ =  bin(int32)[2:]
    binary = '0' * (32-len(bin_)) + bin_
    ipv4 = ["." + str(int(binary[i: i+8], 2)) for i in range(0, 32, 8)]
    return "".join(ipv4)[1:]

if __name__ == "__main__":
    int32_to_ip(396747773)