def one_month(officiators):
    for _ in range(4):
        print_roster(one_week(officiators))
        print("\n")

        for officiator in officiators:
            print(f"{officiator}({officiator.number_of_times_picked})")
            officiator.reset()