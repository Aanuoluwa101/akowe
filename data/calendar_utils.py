import calendar
from datetime import datetime
import json
import os


def month_service_days(year, month):
    service_days = {calendar.WEDNESDAY: "Wednesday", calendar.FRIDAY: "Friday", calendar.SUNDAY: "Sunday", calendar.THURSDAY: "Thursday"}
    month_matrix = calendar.monthcalendar(year, month)
    services = {}

    for week in month_matrix:
        for day in week:
            if day != 0:
                weekday = calendar.weekday(year, month, day)
                if (weekday in service_days and weekday != 3) or (weekday == 3 and day <= 7):  
                    service_date = datetime(year, month, day).strftime('%d-%m-%Y')
                    service_day = service_days[weekday]
                    services[service_date] = service_day
            else:
                continue
    return services

def year_service_days(year):
    for i in range(1, 13):
        month_dir = f"years/{year}/{calendar.month_name[i]}"

        if not os.path.exists(month_dir):
            os.mkdir(month_dir)
        month_file = f"{month_dir}/service_days.json"
        services = month_service_days(year, i)
        with open(month_file, "w") as json_file:
            json.dump(services, json_file, indent=2)
            
def make_year(year):
    year_dir = f"years/{year}"
    if not os.path.exists(year_dir):
        os.makedirs(f"years/{year}")
    year_service_days(year)

if __name__ == "__main__":
    #make_year(2024)
    year = 2024
    month = "July"
    month_idx = 7
    service_days = month_service_days(year, month_idx)
    dir_path = f"./years/{year}/{month}"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    file_path = f"{dir_path}/services.json"
    with open(file_path, "w") as jfile:
        json.dump(service_days, jfile, indent=2)


