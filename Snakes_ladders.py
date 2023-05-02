# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python
# 5 kyu

from random import *

class SnakesLadders():
    
    def __init__(self):
        self.positions = [0, 0] #P1 - 0 / P2 - 1
        self.player = 0
        self.p_pos = 0
        self.count = 1
        self.win = False

        self.special = { "2" : 38,
                         "7" : 14,
                         "8" : 31,
                         "15": 26,
                         "16": 6,
                         "21": 42, 
                         "28": 84,
                         "36": 44,
                         "46": 25,
                         "49": 11,
                         "51": 67,
                         "62": 19,
                         "64": 60,
                         "71": 91,
                         "74": 53,
                         "78": 98,
                         "87": 94,
                         "89": 68,
                         "92": 88,
                         "95": 75,
                         "99": 80}

    def set_player_pos(self, pl, pos, key):
        if key == "Update":
            self.positions[pl] += pos
        else:
            self.positions[pl] = pos
        
        self.p_pos = self.positions[pl]
    
    def get_player_pos(self, pl):
        return self.positions[pl]
    
    def check_special(self):
        self.set_player_pos(self.player, self.special.get(str(self.p_pos), self.p_pos), "Set")

    def play(self, die1, die2):
        
        if self.win:
            return "Game over!"
        
        #update pos with new roll
        self.set_player_pos(self.player, die1 + die2, "Update") 

        #Check if there is any "bounce-back"
        if self.p_pos > 100:
            self.set_player_pos(self.player, (100 - (self.p_pos - 100)), "Set")
            
        elif self.p_pos == 100: #Winner
            self.win = True
            return f"Player {self.player + 1} Wins!"
        
        #checking if its a special instance
        self.check_special()

        output = f"Player {self.player + 1} is on square {self.get_player_pos(self.player)}"
    
        if die1 == die2:
            pass
        else:
            self.player = self.count % 2   #will always alternate between 1 and 0 (odd and even) 
            self.count += 1  
        
        return output
