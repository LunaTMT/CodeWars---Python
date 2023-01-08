# https://www.codewars.com/kata/536e9a7973130a06eb000e9f/python
# Kata Author: yaphi1
# 6 kyu

def calculate_damage(t1, t2, att, def_):
    dict_ = {
        'fire':      ['g', [['f'], 'e'], 'w'],
        'water':     ['f',  ['w'], 'g' , 'e'],
        'grass':     ['w', [['g'], 'e'], 'f'],
        'electric':  ['w', [['e'], 'g' , 'f']] }
        
    row = dict_[t2]
        
    if t1[0] in row: 
        if row.index(t1[0]) > 1:
            eff = 2
        else:
            eff = 0.5
    else:  
        if t1[0] not in row[1][0]:
            eff = 1
        else:
            eff = 0.5
                
    return  50 * (att / def_) * eff
        
if __name__ == "__main__":
    calculate_damage("electric", "fire", 100, 100)   #, 50)
    calculate_damage("grass", "electric", 57, 19)    #, 150)
    calculate_damage('water', 'water', 16, 1)        #, 50)
    calculate_damage("grass", "electric", 57, 19)    #, 150)
    calculate_damage("grass", "water", 40, 40)       #, 100)
    calculate_damage("grass", "fire", 35, 5)         #, 175)
    calculate_damage("fire", "electric", 10, 2)      #, 250)
