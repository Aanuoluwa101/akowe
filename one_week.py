def one_week(officiators):
    WEEKLY_SLOTS = 10
    slot_per_officiator = math.ceil(WEEKLY_SLOTS / len(officiators))

    #print(slot_per_officiator)


    roster = [pick_multiple(3, officiators, slot_per_officiator) for _ in range(2)]
    roster.append(pick_multiple(4, officiators, slot_per_officiator))
    print(len(officiators))
    return roster

