from data import conductors, readers, preachers
from data import friday as fri
from data import sunday as sun
import random
import math

if __name__ == "__main__":
    #say this is the chooser
    services = [fri, sun]
    service_count = 2
    lesson_count = 3
    sermon_count = 2

    conductors_copy = conductors.copy()
    readers_copy = readers.copy()
    preachers_copy = preachers.copy()

    conduction_limit = math.ceil(service_count / len(conductors))
    read_limit = math.ceil(lesson_count / len(readers))
    preach_limit = math.ceil(sermon_count / len(preachers))

    #conductors = ["Mercy", "John", "Jude", "Joshua"]
    #readers = ["Mercy", "John", "Jude", "Joshua"]
    #preachers = ["Mercy", "John", "Jude", "Joshua"]
    #will it ever happen that we remove and don't have anybody to pick?


    #pick conductor
    
    for service in services:
        conductor = random.choice(conductors_copy)
        while conductor.conduction_count >= conduction_limit:
            popped = conductors_copy.pop(conductors_copy.index(conductor))
            conductor = random.choice(conductors_copy)

            
        service.conductor = conductor.name
        conductor.conduction_count += 1


        print(service)
        print(conductor)
        print("\n")