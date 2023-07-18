def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0
    for period in permanence_period:
        start, end = period
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        if start <= target_time <= end:
            counter += 1
    return counter

print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
