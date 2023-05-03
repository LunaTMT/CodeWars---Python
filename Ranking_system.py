# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method


class User:

    def __init__(self) -> None:
        self.rank = -8
        self.progress = 0
        
        self.rank_idx = 0
        self.ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]


    def update_points(self, new_rank):
        rank = self.rank

        if rank == 8:
            return
        
        higher = max([rank, new_rank])
        lower = min([rank, new_rank])
        diff = higher - lower
            
        if (higher > 0 and lower < 0) :
            diff -= 1
    
        if new_rank < rank:
            diff *= -1


        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        elif diff <= -2:
            pass
        else:
            self.progress += 10 * (abs(diff)**2)


    def inc_progress(self, new_rank):
        
        if new_rank not in self.ranks:
            raise Exception
 
        self.update_points(new_rank)


        if self.progress >= 100:
            q, self.progress = divmod(self.progress, 100)
            
            self.rank_idx += q
            if self.rank_idx >= 15:
                self.rank_idx = 15
                self.progress = 0
            
            self.rank = self.ranks[self.rank_idx]

