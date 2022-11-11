import numpy as np

def rgb(r, g, b):
    colours = [r, g, b]
    hex = []

    base_hex_codes = {
                0:['0','0'],
                1:['0','1'],
                2:['0','2'],
                3:['0','3'],
                4:['0', '4'],
                5:['0','5'],
                6:['0','6'],
                7:['0','7'],
                8:['0','8'],
                9:['0','9']}

    hex_codes = {
                0:'0',
                1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9',
                10:'A',
                11:'B',
                12:'C',
                13:'D',
                14:'E',
                15:'F'}

    for value in colours:
        if value <= 0:
            hex.append(['0', '0'])
        elif value >= 255:
            hex.append(['F', 'F'])
        elif 1 <= value <= 9:
            hex.append(base_hex_codes[value])
        else:
            result = value
            storage = []
            while result > 1:
                     result /= 16
                     storage.append(hex_codes[int((result % 1) * 16)]) 
            hex.append(storage[::-1])

    print(colours)
    return "".join(np.array(hex).flatten())


if __name__ == "__main__":
        rgb(-6, 200, 10)
        rgb(56, 35, 26)
        rgb(0, 0, 0)#, "000000", "testing zero values")
        rgb(1, 2, 3)#, "010203", "testing near zero values")
        rgb(255, 255, 255)#, "FFFFFF", "testing max values")
        rgb(254, 253, 252)#, "FEFDFC", "testing near max values")
        rgb(-20, 275, 125)#, "00FF7D", "testing out of range values")
        
# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python            jhoffner

""" 
best solution 

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""
       
