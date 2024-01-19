import random

def pick_again(officiators, name):
    #list must be at least 2 long
    officiator =  random.choice(officiators)
    while officiator.name == name:
        officiator =  random.choice(officiators)

    return officiator