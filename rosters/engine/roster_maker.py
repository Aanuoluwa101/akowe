import json
import os
from .chooser import Chooser
from .service import Service
from .officiator_dto import OfficiatorDto

class RosterMaker:
    def make_services(self, month, year, lesson_file):
        services = []
        service = {}
        services_file = f"./data/years/{year}/{month}/services.json"
        lesson_file = f"./data/years/{year}/{month}/{lesson_file}"
        # services_file = f"../../data/years/{year}/{month}/services.json"
        # lesson_file = f"../../data/years/{year}/{month}/{lesson_file}"
        try:
            with open(services_file, "r") as json_file:
                service_days = json.load(json_file)

            #ignore lessons for now
            with open(lesson_file, "r") as json_file:
                lessons = json.load(json_file)

            for date, day in service_days.items():
                #service["first_lesson"] = "Deut 23:3-5"
                service.update(lessons[date])
                service["date"] = date
                service["day"] =  day

                if day == "Wednesday" or day == "Friday" or day == "Thursday":
                    service["type"] = "weekday"
                    #service["second_lesson"] = None
                elif day == "Sunday":
                    service["type"] = "sunday"
                    #service["second_lesson"] = "Matthew 2:2-10"

                services.append(Service(**service))
        except (IndexError, FileNotFoundError) as e:
            print(f"An error occurred while making services: {e}")
            return None

        return services

    def make_roster(self, data):
        # user_id, month, year, lesson_file, officiators = data["user_id"], data["month"], \
        #                      data["year"], data["bible_lesson_file"], data["officiators"]

        #for TESTING
        username, email, month, year, lesson_file, officiators = data["temp_user"], data["email"], data["month"], \
                             data["year"], data["bible_lesson_file"], data["officiators"]
        
        # roster_dir = f"data/users/{user_id}/rosters/{year}"
        #for Testing
        roster_dir = f"data/users/{username}/rosters/{year}"
        if not os.path.exists(roster_dir):
            os.makedirs(roster_dir)
        roster_file = os.path.join(roster_dir, f"{month}.json")
        
        def save_roster_to_file(services, roster_metadata, roster_file):
            services_and_officiators = []
            roster = {}
            for service in services:
                services_and_officiators.append(service.to_dict())

            roster.update(roster_metadata)
            roster["roster"] = services_and_officiators
            
            with open(roster_file, "w") as json_file:
                json.dump(roster, json_file, indent=2)
            return roster
        
        try:
            #we comment this out because officiators are already made from the data file
            officiators = [OfficiatorDto(**officiator) for officiator in officiators]
            services = self.make_services(month, year, lesson_file)
            if not services or not officiators:
                raise ValueError("no officiators or could not make services")
            chooser = Chooser(officiators, services)
            
            chooser.choose()
            # roster_metadata = {"user_id": user_id, "month": month, "year": year}
            #For TESTING
            roster_metadata = {"username": username, "email": email, "month": month, "year": year}
            roster = save_roster_to_file(services, roster_metadata, roster_file)
            return roster
            #return {"roster": ['roster']}
        except Exception as e:
            print(f"Error making roster: {e}")
            raise e
        
if __name__ == "__main__":
    rm = RosterMaker()
    services = rm.make_services("April", 2024, "bible_lessons_d.json")
    for service in services:
        print(service.neonate_to_dict())
