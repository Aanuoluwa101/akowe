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

    #conductors = ["Mercy(2)", "John(1)", "Jude(3)", "Joshua(4)"]
    #readers = ["Mercy", "John", "Jude", "Joshua"]
    #preachers = ["Mercy", "John", "Jude", "Joshua"]
    #will it ever happen that we remove and don't have anybody to pick?


    
    #go through the services
    for service in services:
        #pick conductor
        print("picking conductor")
        conductor = random.choice(conductors_copy)
        while conductor.conduction_count >= conduction_limit:     #limit consideration
            popped = conductors_copy.pop(conductors_copy.index(conductor))
            # if len(conductors_copy) == 0:
            #     break
            conductor = random.choice(conductors_copy)
        service.conductor = conductor
        conductor.conduction_count += 1

        #pick lesson reader
        reader = random.choice(readers_copy)
        while reader.read_count >= read_limit:   #limit consideration 
            #popped = readers_copy.pop(readers_copy.index(reader))  #there will always be an officiator
                                                                    #because the total sum of limit exceeds the number of readings
            reader = random.choice(readers_copy)

            #don't duplicate until 

        try:
            while reader.rank < service.conductor.rank or reader == service.conductor:
                popped = readers_copy.pop(readers_copy.index(reader))  #if we don't need pop, change to remove
                print(f"removing {reader.name} due to lower rank({reader.rank})")

                reader = random.choice(readers_copy)  #there is automatic duplication in case of not finding appropriate rank
            service.first_lesson_reader = reader
            conductor.read_count += 1
        except IndexError:   #there is nobody in the readers list with a rank equal to or higher than the conductor's
            #do a move up of the conductor (but only if they can read)
            if service.conductor.can_read:
                #find all lower or equal ranks in conductors
                lower_or_equal_ranks = []
                for conductor in conductors:
                    if conductor.rank <= service.conductor:
                        lower_or_equal_ranks.append(conductor)
                if len(lower_or_equal_ranks) > 0:  
                    for condcutor in lower_or_equal_ranks:
                        if condcutor.conduction_count < conduction_limit:  #someone with lower rank and within limit
                            service.first_lesson_reader = conductor   #set the reader to the current conductor (move the conductor up)
                            service.conductor = conductor
                    #nobody within limit
                    service.first_lesson_reader = conductor  #move up
                    service.conductor = random.choice(lower_or_equal_ranks) #choose anyone, allowing them to exceed limit

                else:  #nobody of lower rank. is it possible that we don't find someone not lower or equal to? 
                       #no. except he's the only one on the list which we will not allow
                    pass
                        


                        

        print(service)
        print(conductor)
        print("\n")