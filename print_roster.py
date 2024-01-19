def print_roster(roster):
    for service in roster:
        if len(service) == 3:
            print(f"    {service[0]}  {service[1]}  nil  {service[2]}\n")
        else:
            print(f"    {service[0]}  {service[1]}  {service[2]}  {service[3]}\n")