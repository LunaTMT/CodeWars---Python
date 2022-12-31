from functools import reduce

def ips_between(start, end):
    start = list(map(int, start.split('.')))    #[20, 0, 0, 10]
    end = list(map(int, end.split('.')))        #[20, 0, 1,  0]

    #[0, 0, 256, -10]
    diff = [(value - start[i]) * (pow(256, len(end)-i-1)) for i, value in enumerate(end) ]

    #Summing the different list for all values that are not 0 (via filter)
    return sum(list(filter(lambda num: num != 0, diff)))

    


if __name__ == "__main__":
    ips_between("20.0.0.10", "20.0.1.0")