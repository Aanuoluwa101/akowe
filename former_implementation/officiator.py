import math
# from print_roster import print_roster
# from pick_multiple import pick_multiple


class Officiator:
    count = 1
    
    def __init__(self, name, rank, can_conduct, can_read, can_preach, on_weekday, on_sunday, enforcements):
        self.id = Officiator.count
        self.name = name
        self.rank = rank
        
        self.can_conduct = can_conduct
        self.can_read = can_read
        self.can_preach = can_preach

        # self.on_wednesday = on_wednesday
        # self.on_friday = on_friday
        
        self.on_weekday = on_weekday
        self.on_sunday = on_sunday

        self.conduction_count = 0
        self.read_count = 0
        self.preach_count = 0

        self.enforcements = enforcements  #list of dictionaries (date, officiation)
        #max number will be global but when being used, len(enforcements) will be factored in
        Officiator.count += 1

    def __str__(self):
        return f"{self.name}: rank={self.rank}, can_conduct({self.can_conduct}), can_read({self.can_read}), \
can_preach({self.can_preach}), weekday({self.on_weekday}), sunday({self.on_sunday}), \
conduct_count({self.conduction_count}), read_count({self.read_count}), preach_count({self.preach_count})"

    def reset(self):
        self.number_of_times_picked = 0




        

    

    
