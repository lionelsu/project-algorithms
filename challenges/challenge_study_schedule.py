def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    count = 0

    for start, finish in permanence_period:
        if not isinstance(start, int) or not isinstance(finish, int):
            return None
        if start <= target_time <= finish:
            count += 1
    return count
