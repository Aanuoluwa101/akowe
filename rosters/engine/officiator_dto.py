import math
# from print_roster import print_roster
# from pick_multiple import pick_multiple


class OfficiatorDto:
    count = 1
    name = ""
    email = ""
    phone = ""
    rank = None
    can_conduct_on_weekdays = False
    can_conduct_on_sundays = False
    can_read_on_weekdays = False
    can_read_on_sundays = False
    can_preach_on_weekdays = False
    can_preach_on_sundays = False

    #during the creation of an officiator, use the chosen ranking to assign values
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   

        self.officiation_count = {"conductor": {"weekday": 0, "sunday": 0}, 
                                  "first_lesson_reader": {"weekday": 0, "sunday": 0},
                                  "second_lesson_reader": {"weekday": 0, "sunday": 0},
                                  "preacher": {"weekday": 0, "sunday": 0}}
        
        self.officiation_count_special = {"conductor": {"weekday": 0, "sunday": 0}, 
                                  "first_lesson_reader": {"weekday": 0, "sunday": 0},
                                  "second_lesson_reader": {"weekday": 0, "sunday": 0},
                                  "preacher": {"weekday": 0, "sunday": 0}}
        
        self.rank_and_name = f"{self.rank['short']} {self.name}"

        # self.enforcements = enforcements  #list of dictionaries (date, officiation)
        #max number will be global but when being used, len(enforcements) will be factored in
        #Officiator.count += 1

    def get_officiation_count(self, officiation, service_type):
        return self.officiation_count[officiation][service_type]
    
    def increment_officiation_count(self, officiation, service_type):
        self.officiation_count[officiation][service_type] += 1

    

    def __str__(self):
        return f"{self.name}: rank={self.rank}, can_conduct({self.can_conduct}), can_read({self.can_read}), \
can_preach({self.can_preach}), weekday({self.on_weekday}), sunday({self.on_sunday}), \
conduct_count({self.conduction_count}), read_count({self.read_count}), preach_count({self.preach_count})"
    
    


