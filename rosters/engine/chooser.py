import random
import math
from .officiator_dto import OfficiatorDto
from .service import Service

class Chooser:
    def __init__(self, all_officiators, services):
        self.services = services
        if len(all_officiators) >= 5:
            self.officiation_per_service = 1
        else: 
            self.officiation_per_service = 2

        self.officiation_info = {"conductor": {"officiation_count": "conduction_count", "pool": {}, "limit": {}},
                                 "first_lesson_reader": {"officiation_count": "read_count", "pool": {}, "limit": {}},
                                 "second_lesson_reader": {"officiation_count": "read_count", "pool": {}, "limit": {}},
                                 "preacher": {"officiation_count": "preach_count", "pool": {}, "limit": {}}}

        self.officiation_info["conductor"]["pool"]["weekday"] = [officiator for officiator in all_officiators if officiator.can_conduct_on_weekdays]
        self.officiation_info["conductor"]["pool"]["sunday"] = [officiator for officiator in all_officiators if officiator.can_conduct_on_sundays]
        self.officiation_info["first_lesson_reader"]["pool"]["weekday"] = [officiator for officiator in all_officiators if officiator.can_read_on_weekdays]
        self.officiation_info["first_lesson_reader"]["pool"]["sunday"] = self.officiation_info["second_lesson_reader"]["pool"]["sunday"] = [officiator for officiator in all_officiators if officiator.can_read_on_sundays]
        self.officiation_info["preacher"]["pool"]["weekday"] = [officiator for officiator in all_officiators if officiator.can_preach_on_weekdays]
        self.officiation_info["preacher"]["pool"]["sunday"] = [officiator for officiator in all_officiators if officiator.can_preach_on_sundays]

        self.prepare_data()

        self.officiation_info["conductor"]["limit"]["weekday"] = math.ceil(self.data["weekday_services"] / len(self.officiation_info["conductor"]["pool"]["weekday"]))
        self.officiation_info["conductor"]["limit"]["sunday"] = math.ceil(self.data["sunday_services"] / len(self.officiation_info["conductor"]["pool"]["sunday"]))
        self.officiation_info["first_lesson_reader"]["limit"]["weekday"] = math.ceil(self.data["weekday_readings"] / len(self.officiation_info["first_lesson_reader"]["pool"]["weekday"]))
        self.officiation_info["first_lesson_reader"]["limit"]["sunday"] = self.officiation_info["second_lesson_reader"]["limit"]["sunday"] = math.ceil(self.data["sunday_readings"] / len(self.officiation_info["first_lesson_reader"]["pool"]["sunday"]))
        self.officiation_info["preacher"]["limit"]["weekday"] = math.ceil(self.data["weekday_sermons"] / len(self.officiation_info["preacher"]["pool"]["weekday"]))
        self.officiation_info["preacher"]["limit"]["sunday"] = math.ceil(self.data["sunday_sermons"] / len(self.officiation_info["preacher"]["pool"]["sunday"]))


        self.settle_enforcements(services, all_officiators)

    def prepare_data(self):
        self.data = {}

        weekday_services = weekday_readings = weekday_sermons = 0
        sunday_services = sunday_readings = sunday_sermons = 0

        for service in self.services:
            if service.type == 'sunday':
                if not service.conductor:
                    sunday_services += 1
                if not service.first_lesson_reader and not service.second_lesson_reader:
                    sunday_readings += 2
                elif (service.first_lesson_reader and not service.second_lesson_reader) or (not service.first_lesson_reader and service.second_lesson_reader):
                    sunday_readings += 1
                if not service.preacher:
                    sunday_sermons += 1
            else:
                if not service.conductor:
                    weekday_services += 1
                if not service.first_lesson_reader:
                    weekday_readings += 1
                if not service.preacher:
                    weekday_sermons += 1

        self.data["weekday_services"] = weekday_services
        self.data["weekday_readings"] = weekday_readings
        self.data["weekday_sermons"] = weekday_sermons
        self.data["sunday_services"] = sunday_services
        self.data["sunday_readings"] = sunday_readings
        self.data["sunday_sermons"] = sunday_sermons

            
    def set_officiator(self, service, officiation_type):
        if service.__getattribute__(officiation_type):
            return
        
        officiation = self.officiation_info[officiation_type]
        pool, limit = officiation["pool"][service.type], officiation["limit"][service.type]

        buffer = []

        officiator = random.choice(pool)
        officiation_count = officiator.get_officiation_count(officiation_type, service.type)
        while officiation_count >= limit or not self.rank_check(service, officiator, officiation_type) or service.officiators.count(officiator) >= self.officiation_per_service:   
            popped = pool.pop(pool.index(officiator))
            #print(f"removing {popped.name}")
            buffer.append(popped)
            #everybody don finish
            if len(pool) == 0:
                #print(f"setting {officiation_type}")
                adhoc_pool = pool + buffer
                officiator = self.recover(service, officiation_type, adhoc_pool)
                if not officiator:
                    print("couldn't get a replacement, picking anybody")
                    officiator = random.choice(adhoc_pool)
                    #officiator = self.default
                break
            else:
                officiator = random.choice(pool)
                officiation_count = officiator.get_officiation_count(officiation_type, service.type)
        
        service.set_officiator(officiation_type, officiator)
        officiator.increment_officiation_count(officiation_type, service.type)
        self.officiation_info[officiation_type]["pool"][service.type].extend(buffer)


    def recover(self, service, officiation_type, pool):    
        if service.type == "weekday":
            rank_order = ["conductor", "first_lesson_reader", "preacher"]
        elif service.type == "sunday":
            rank_order = ["conductor", "first_lesson_reader", "second_lesson_reader", "preacher"]

        officiation_idx = rank_order.index(officiation_type)
        if officiation_type == "conductor": #I doubt if this will ever happen sha
            return random.choice(pool)
        else:
            officiator_before = service.__getattribute__(rank_order[officiation_idx - 1])
            min_rank = officiator_before.rank["weight"]

        for officiator in pool:
            #print(f"checking {officiator.name}")
            if officiator.rank["weight"] >= min_rank and officiator.id != officiator_before.id:
                return officiator

    def set_oficiators(self, service):
        self.set_officiator(service, "conductor")
        self.set_officiator(service, "first_lesson_reader")
        if service.type == "sunday":
            self.set_officiator(service, "second_lesson_reader")
        self.set_officiator(service, "preacher")

        

    def rank_check(self, service, potential_officiator, officiation_type):
        if service.type == "weekday":
            rank_order = ["conductor", "first_lesson_reader", "preacher"]
        elif service.type == "sunday":
            rank_order = ["conductor", "first_lesson_reader", "second_lesson_reader", "preacher"]

        officiation_idx = rank_order.index(officiation_type)
        
        def check_before_rank():
            return potential_officiator.rank["weight"] >= service.__getattribute__(rank_order[officiation_idx - 1]).rank["weight"]
            
        def check_after_rank():
            return potential_officiator.rank["weight"] <= service.__getattribute__(rank_order[officiation_idx + 1]).rank["weight"]


        check_passed = True 
        if officiation_type == "first_lesson_reader" or officiation_type == "second_lesson_reader":
            if service.__getattribute__(rank_order[officiation_idx + 1]):
                check_passed = all([check_before_rank(), check_after_rank()])
            else:
                check_passed = check_before_rank()
        #if someone after
        elif officiation_type == "conductor" and service.__getattribute__(rank_order[officiation_idx + 1]):
            check_passed = check_after_rank()
        elif officiation_type == "preacher":
            check_passed = check_before_rank()
        return check_passed

    #what is the name of the person we are talking about
      

    def settle_enforcements(self, services: list[Service], officiators: list[OfficiatorDto]) -> None:
        def find_service(date: str)-> Service:
            for service in services:
                if service.date == date:
                    return service
    
        for officiator in officiators:
             for enforcement in officiator.enforcements:
                service = find_service(enforcement["date"])
                if not service:
                    raise ValueError("Service not found")
                service.__setattr__(enforcement["officiation"], officiator)

                officiator.increment_officiation_count(enforcement["officiation"], enforcement["service_type"])

    def choose(self):
        for service in self.services:
            self.set_oficiators(service)
    
        