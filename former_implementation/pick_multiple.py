from pick_again import pick_again
from pick_one import pick_one

def pick_multiple(how_many, officiators, slot_per_officiator):
    lst = []
    for _ in range(how_many):
        officiator = pick_one(officiators, slot_per_officiator)
        #print(len(officiators))

        #pick again #this is the center that controls repitition
        if len(officiators) <= 4 and lst.count(officiator) >= 1:
            officiator = pick_again(officiators, officiator.name)
        elif lst.count(officiator) >= 1:
            officiator = pick_again(officiators, officiator.name)

        lst.append(officiator)
        officiator.number_of_times_picked += 1
    return lst