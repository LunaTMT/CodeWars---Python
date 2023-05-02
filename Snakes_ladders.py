from random import *
from collections import defaultdict

class SnakesLadders():

    def __init__(self):
        self.positions = [0, 0] #P1 - 0 / P2 - 1
        self.player = 0
        self.p_pos = 0
        self.count = 1

    
        
        self.special = { "2" : 38,
                         "7" : 14,
                         "8" : 31,
                         "15": 26,
                         "16": 6,
                         "28": 84,
                         "21": 42,
                         "36": 44,
                         "46": 25,
                         "49": 11,
                         "51": 57,
                         "62": 19,
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
    

    def play(self, die1, die2):

        sum_ = die1 + die2
        
        #update pos with new roll
        self.set_player_pos(self.player, sum_, "Update") 

        #checking if its a special instance
        self.set_player_pos(self.player, self.special.get(str(self.p_pos), self.p_pos), "Set")

        #Check if there is any "bounce-back"
        if self.p_pos > 100:
            self.set_player_pos(self.player, (100 - self.p_pos - 100), "Set")

        
        output = f"Player {self.player + 1} is on square {self.get_player_pos(self.player)}"
        
        if die1 == die2:
            pass
        else:
            self.player = self.count % 2   #will always alternate between 1 and 0 (odd and even) 
            self.count += 1  
        
        return output
            
            

if __name__ == "__main__":
    game = SnakesLadders()
    game.play(1, 1)
    game.play(1, 5)