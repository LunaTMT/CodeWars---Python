from collections import deque 
import numpy as np
def recoverSecret(triplets):
    
    char = sorted(list(set("".join(np.array(triplets).flatten(order='C')))))
    keys = [{'left': "", 'right': ""} for i in (range(0,len(char)))]
    pos = dict(zip(char, keys))
    
    for triplet in triplets:
        for idx, value in enumerate(triplet):
            pos[value]['left'] = "".join(set( pos[value]['left'] + "".join(triplet[:idx])))
            pos[value]['right'] = "".join(set( pos[value]['right'] + "".join(triplet[idx+1:])))
           
    secret = deque([])
    
    for idx, (key, value) in enumerate(pos.items()):

        left = sum([True if secret.count(i) >= 1 else False for i in value['left'] ])
        right = sum([True if secret.count(i) >= 1 else False for i in value['right'] ])
        
       

        if not left and not right:
            secret.append(key) #first - a

        elif not value['left']: 
            start = key 
        elif not value['right']:
            end = key

        elif left and right:
            
            indexes = [secret.index(val) for idx, val in enumerate(secret) if val in value['left']]

            secret.insert(indexes[-1] + 1, key)

        else: # (left or right):
            if right:
                secret.appendleft(key)
            elif left:
                secret.append(key)

    return start + "".join(secret) + end
        
        
    
        
        #print(f"\n{key} {value}, \n[left : {left} right : {right}]\n")


if __name__ == "__main__":
    secret = "whatisup"
    triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
    ]

    recoverSecret(triplets)
                    
        
                