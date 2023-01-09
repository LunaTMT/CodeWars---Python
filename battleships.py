

import os

import pprint as pp

def too_close(position, field):
    i, j = position

    corners = {
            'LC' : (i-1, j-1),
            'RC' : (i-1, j+1),
            'BL' : (i+1, j-1),
            'BR' : (i+1, j+1)  }

    for key in corners:
        try:
            i, j = corners[key]
            if i >= 0 and j >= 0:
                if field[i][j] == 1:
                    return True
        except:
            pass
    return False


def get_next(position, count, card):
    i, j = position
    cardinals = {
        'n' : ( i - (1 * count)   , j),
        'e' : ( i       , j + (1 * count)),
        's' : ( i + (1 * count)   , j),
        'w' : ( i       , j - (1 * count))}

    return cardinals[card]

def find_length(position, field):
    i, j = position
    field[i][j] = '_'

    if too_close(position, field):
        return False

    card = ['n', 'e', 's', 'w']
    found = False
    count = 1

    for card in card:
        if found == True:
            break
        count = 1

        while True:
            i, j = get_next(position, count, card )
            if i >= 0 and j >= 0:
                try:
                    if field[i][j] == 1:
                        if too_close((i, j), field):
                            return False

                        field[i][j] = '_'
                        found = True
                        count += 1
                    else:
                        break
                except:
                    break
            else:
                break
   
    return count
    

def validate_battlefield(field):
    clear = lambda: os.system('clear')
    

    if sum([i.count(1) for i in field]) != 20:
        return False
    
    counts = {
        1: [0, 4],
        2: [0, 3],
        3: [0, 2],
        4: [0, 1] }

    
    for i, row in enumerate(field):
        for j, item in enumerate(row):
            if item == 1:
                count = find_length((i,j), field)
                if count == False:
                    return False

                counts[count][0] += 1

                clear()
                pp.pprint(field)
                print()

               
                if counts[count][0] > counts[count][1]:
                    return False
              
    return True if all([True if counts[i][0] == counts[i][1] else False for i in counts]) else False


if __name__ == "__main__":
    battleField =  [[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]


    validate_battlefield(battleField)   #, True, "Yep! Seems alright", "Nope, something is wrong!");               