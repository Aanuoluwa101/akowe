import random
from officiator import Officiator

def pick_one(officiators: list, slot_per_officiator: int) -> Officiator:
    # increase count if count is less than average pick time
    # if the person picked has occured twice (set average), remove them and pick again
    officiator = random.choice(officiators)
    #print(f"picked {officiator.name}")

    removed = []
    #this logic should not be here
    while officiator.number_of_times_picked >= slot_per_officiator and len(officiators) > 0:
        popped = officiators.pop(officiators.index(officiator))
        removed.append(popped)
       # print(f"removing {popped.name}")
        #print(f"removed {officiator.name}")
        officiator = random.choice(officiators)

    officiators += removed
    return officiator
