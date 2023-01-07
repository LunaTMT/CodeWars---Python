import numpy as np

def get_dict(dict_items, row):
    return ([[k for k, v in dict_items if v == idx][0] for idx in row])


def flap_display(lines, rotors):
    values = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789']
    letters = [[*"".join(row)] for row in lines]
    
    dict = {values[i] : i for i in range(0, len(values))} 
    idx = [[dict[i] for i in row] for row in letters ]
    cum_idx = [np.cumsum(row) for row in rotors]
    new_idx = list(map(lambda x, y: (x + y) % 54, idx, cum_idx))

    return  ["".join(get_dict(dict.items(), row)) for row in new_idx]
    
if __name__ == "__main__":
    lines = ['+---------------------------+', 
             '| THIS IS A MULTI LINE TEST |',   
             '+---------------------------+']

    rotors = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53], 
              [8, 46, 7, 12, 30, 1, 4, 16, 34, 52, 32, 13, 11, 48, 3, 14, 4, 24, 16, 13, 3, 47, 22, 26, 50, 13, 52, 47, 8], 
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53]]
    flap_display(lines, rotors)

