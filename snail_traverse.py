#kata author: stevenbarragan
#4kyu
#Snail Traverse an array
#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

import numpy as np
import math
from itertools import chain


def snail(snail):
    snail = np.array(snail)
    size = snail.size

    even = False
    #even / odd base number clasification based on size of array
    if (size % 2) == 0:
        even = True  #even
    else:
        even = False  #odd
    
    answer = []
     
    r, c = snail.shape
    size = snail.size
    r_idx = r - 1
    c_idx = c - 1
    i = 0
   
    while True:
        #Odd even class
        if even == True:
            if(len(answer)) >= ((2*r - 1) - 1):
                break
            else:
                pass
        else:
            if(len(answer)) >= ((2*r - 1) - 1):
                #append centre value
                centre = math.trunc(r/2)
                answer.append([snail[centre][centre]])
                break
            else:
                pass
        
        #slicing edge at init
        if i == 0:
            top = snail[0+i]
            right = snail[1:, c_idx]
            bottom = snail[r_idx, :c_idx][::-1]
            left = snail[:, 0][::-1][1:-1]
        
        #slicing edge for values of i, whereby 'i' is next inner square
        else: 
            top = snail[0+i][i:-i]
            right = snail[1+i:, c_idx-i][:-i]
            bottom = snail[r_idx-i, :c_idx][::-1][i:-i]
            left = snail[:, i][::-1][i+1:-i-1]


        answer.append(top)
        answer.append(right)
        answer.append(bottom)
        answer.append(left)

        i += 1
    
    return list(chain.from_iterable(answer))

if __name__ == "__main__":

    array = [[1,  2 , 3,  4,  5,  6],
            [22, 23, 24, 25, 26,  7],
            [21, 36, 37, 38, 27,  8],
            [20, 35, 42, 39, 28,  9],
            [19, 34, 41, 40, 29, 10],
            [18, 33, 32, 31, 30, 11],
            [17, 16, 15, 14, 13, 12]]
    snail(array)


    array = [[ 1,  2,  3,  4],
            [ 12, 13, 14,  5],
            [ 11, 16, 15,  6],
            [ 10,  9,  8,  7]]
    snail(array)    # [1,2,3,6,9,8,7,4,5]
    

    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    snail(array)    # [1,2,3,4,5,6,7,8,9]

    array = [   [693, 666, 163, 388, 360, 429], 
        [736, 495, 367, 502, 265, 670], 
        [144, 218, 332, 203, 780, 286], 
        [428, 440, 73, 454, 696, 300], 
        [209, 872, 783, 337, 411, 285], 
        [906, 49, 199, 171, 422, 998]]   
    # [693, 666, 163, 388, 360, 429, 670, 286, 300, 285, 998, 422, 171, 199, 49, 906, 209, 428, 144, 736, 495, 367, 502, 265, 780, 696, 411, 337, 783, 872, 440, 218, 332, 203, 454, 73]
    snail(array)

    array = [
        [627, 583, 538, 714, 85,  998, 139, 559, 855, 754, 527, 520, 889, 80,  127, 400], 
        [82,  669, 159, 796, 930, 709, 508, 605, 281, 611, 911, 526, 168, 728, 840, 874], 
        [589, 712, 231, 333, 504, 112, 973, 981, 755, 146, 231, 73,  967, 61, 828, 318], 
        [992, 538, 846, 532, 800, 188, 562, 835, 807, 830, 855, 258, 494, 675, 286, 932], 
        [969, 992, 265, 984, 879, 180, 529, 808, 329, 296, 964, 88, 37, 958, 163, 398], 
        [887, 569, 369, 801, 889, 560, 433, 34, 966, 177, 333, 196, 60, 609, 853, 912], 
        [644, 275, 331, 718, 259, 758, 649, 620, 621, 566, 671, 398, 358, 122, 517, 354], 
        [249, 149, 891, 44, 660, 178, 981, 428, 759, 917, 939, 686, 624, 499, 522, 856], 
        [578, 656, 52, 977, 330, 310, 641, 235, 328, 690, 5, 260, 159, 308, 470, 966], 
        [37, 377, 54, 872, 373, 886, 825, 239, 19, 565, 424, 539, 218, 321, 959, 603], 
        [419, 397, 764, 220, 162, 762, 768, 67, 821, 977, 966, 347, 121, 279, 560, 837], 
        [924, 382, 546, 375, 472, 49, 725, 170, 942, 559, 643, 862, 953, 324, 609, 802], 
        [474, 848, 277, 959, 522, 710, 583, 582, 770, 597, 230, 112, 503, 714, 926, 12], 
        [200, 147, 574, 493, 644, 299, 571, 678, 257, 949, 806, 366, 947, 951, 315, 108], 
        [950, 222, 979, 924, 346, 559, 82, 952, 719, 757, 900, 148, 138, 863, 970, 941], 
        [69, 754, 287, 788, 339, 274, 544, 142, 974, 550, 399, 893, 595, 576, 908, 447]]
    snail(array)
