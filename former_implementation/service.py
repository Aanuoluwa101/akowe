from datetime import date

class Service:
    conductor = None   #id of conductor
    first_lesson_reader = None   #a dict (lesson, id of reader)
    second_lesson_reader = None  #a dict  ""
    preacher = None         #id of preacher
    WEEKDAY = "Weekday"
    SUNDAY = "Sunday"
    NEW_MOON = "NewMoon"

    def __init__(self, type: str, date):
        if type.lower() == "weekday":
            self.type = Service.WEEKDAY
        elif type.lower() == "sunday":
            self.type = Service.SUNDAY
        elif type.lower() == "new moon":
            self.type = Service.NEW_MOON
        else: 
            raise ValueError("Type must be one of weekday, sunday or new moon")
        
        self.date = date

    def __str__(self) -> str:
        return f"{self.type} service: conductor={self.conductor.name if self.conductor else self.conductor},\
 first={self.first_lesson_reader.name if self.first_lesson_reader else self.first_lesson_reader}, \
 second={self.second_lesson_reader.name if self.second_lesson_reader else self.second_lesson_reader}, \
 preacher={self.preacher.name if self.preacher else self.preacher}"


if __name__ == "__main__":
    service = Service()
    print(service.conductor)

    

#we still have to control for having one person repeated multiple
#times in a week


#the max number for each person will be calculated in the front
#total - enforcements / number of officiators available
    

# enforced people will have this number minus the number the number of times they were enforced 
#for each category; Given that the number of times they were enforced is less than
#the general one
    
#we do this calculation when setting the max during init. We do it based on the number of enforcements
    

