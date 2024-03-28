from datetime import date
import json

class Service:
    conductor = None 
    first_lesson = None
    first_lesson_reader = None 
    second_lesson_reader = None  
    preacher = None         

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)        
        self.officiators = []

    def set_officiator(self, officiation_type, officiator):
        self.__setattr__(officiation_type, officiator)
        #print(f"{officiation_type} is {self.__getattribute__(officiation_type).name}")
        self.officiators.append(officiator)

    def to_dict(self):
        dict = {
                  "date": self.date,
                  "day": self.day,
                  "conductor": self.conductor.rank_and_name,
                  "first_lesson": {"lesson": self.first_lesson, "reader": self.first_lesson_reader.rank_and_name},
                }
        if self.second_lesson:
            dict["second_lesson"] = {"lesson": self.second_lesson, "reader": self.second_lesson_reader.rank_and_name}
        else:
            dict["second_lesson"] = None

        dict["preacher"] = self.preacher.rank_and_name

        return dict
    
    def neonate_to_dict(self):
        dict = {
                  "date": self.date,
                  "day": self.day,
                  "first_lesson": self.first_lesson,
                }
        if self.second_lesson:
            dict["second_lesson"] = self.second_lesson
        else:
            dict["second_lesson"] = None

        return dict
        #"annotation": "Church Anniversary"

    def __str__(self) -> str:
        return f"{self.day}, {self.date}: conductor={self.conductor.name if self.conductor else self.conductor},\
 first={self.first_lesson_reader.name if self.first_lesson_reader else self.first_lesson_reader}, \
 second={self.second_lesson_reader.name if self.second_lesson_reader else self.second_lesson_reader}, \
 preacher={self.preacher.name if self.preacher else self.preacher}"
    

#we still have to control for having one person repeated multiple
#times in a week


#the max number for each person will be calculated in the front
#total - enforcements / number of officiators available
    

# enforced people will have this number minus the number the number of times they were enforced 
#for each category; Given that the number of times they were enforced is less than
#the general one
    
#we do this calculation when setting the max during init. We do it based on the number of enforcements
    

#fetch the month in
    

