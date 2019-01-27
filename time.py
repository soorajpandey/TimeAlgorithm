if last_time >= first_time:
    return first_time <= this_time <= last_time
else:
    return first_time <= this_time or this_time <= last_time