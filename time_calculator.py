
def add_time(start, duration, starting_day=None):
    list_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    list_meridiem = ['AM', 'PM']
    
    starting_time, start_meridiem = start.split(' ')
    start_meridiem = list_meridiem.index(start_meridiem)
    start_hour, start_min = map(int, starting_time.split(':'))  
    add_hour, add_min = map(int, duration.split(':'))
    
    final_hour, final_min = "", ""
    
    final_hour = str(((start_hour + add_hour) % 12) + ((start_min + add_min) > 59))
    sum_min = (start_min + add_min) % 60
    final_min = str("0" * (sum_min < 10) + str(sum_min))

    h_days = ((start_hour + add_hour) + ((start_min + add_min) > 59)) // 12
    
    final_meridiem = list_meridiem[(start_meridiem + (h_days%2)) % 2]

    if(starting_day):
        starting_day = starting_day[0].upper() + starting_day[1:].lower()
    
    days_later = ""
    if h_days > 3 - start_meridiem:
        n_days = start_meridiem + h_days // 2
        days_later = f"({n_days} days later)"
        if starting_day:
            final_day = list_days[(list_days.index(starting_day) + n_days) % 7]
            days_later = final_day + ' ' + days_later
    elif h_days > 1 - start_meridiem:
        days_later = "(next day)"
        if starting_day:
            days_later = list_days[(list_days.index(starting_day) + 1) % 7] + ' ' + days_later
    
    if days_later and starting_day:
        return f"{final_hour}:{final_min} {final_meridiem}, {days_later}"
    elif days_later:
        return f"{final_hour}:{final_min} {final_meridiem} {days_later}"
    elif starting_day:
        return f"{final_hour}:{final_min} {final_meridiem}, {starting_day}"
    else:
        return f"{final_hour}:{final_min} {final_meridiem}"