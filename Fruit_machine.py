# https://www.codewars.com/kata/590adadea658017d90000039/solutions/python
# Kata Author: adrian.eyre
# 6 kyu

def fruit(reels, spins):
    default_item = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
    scoring = [i for i in range(10, 0, -1)]
    
    dict_ = dict(zip(default_item, scoring))  
    
    items = [reels[i][value] for i, value in enumerate(spins) ]
    unique = set(items)
    
    if len(unique) == 1:
        return dict_[list(items)[0]] * 10
    
    elif len(unique) == 2:
        counts = [items.count(val) for val in unique]
        counts =  [list(a) for a in zip(unique,counts)]
        
        score = 0
        wild = False
        
        for i in counts:
            if i[0] == 'Wild' and i[1] != 2:
                wild = True
            elif i[1] == 2:
                print(dict_[i[0]])
                score += dict_[i[0]]
        
        return score * 2 if wild else score
    else:
        return 0
