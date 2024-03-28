import math
from officiator import Officiator
import random

# if a person gets chosen for the average number of times
# per person for a position, it's only fair. 
def choose_conductor(no_of_services, conductor_pool):
    slots_per_conductor = math.ceil(no_of_services / len(conductor_pool))

    conductor_pool_copy = conductor_pool.copy()
    #buffer = []
    conductors = []
    for _ in range(no_of_services):
        if len(conductor_pool_copy) == 0:
            conductor_pool_copy = conductor_pool.copy
            #buffer = []
        conductor = random.choice(conductor_pool_copy)
        while conductors.count(conductor) >= slots_per_conductor:
            conductor_pool_copy.remove(conductor)
            conductor = random.choice(conductor_pool_copy)
        conductors.append(conductor)
    return conductors

#we want to test that it doesn't line people up


if __name__ == "__main__":
    officiators_list = ["Mercy", "John", "Jude","Joshua", "Jerry", "Ayo", "Wisdom", "King", "Femi", "Ola", "Ini"]
    #, "Joshua", "Jerry", "Ayo", "Wisdom", "King", "Femi", "Ola", "Ini"
    officiators = [Officiator(name) for name in officiators_list]

    conductors = choose_conductor(7, officiators)
    for conductor in conductors:
        print(conductor.name)