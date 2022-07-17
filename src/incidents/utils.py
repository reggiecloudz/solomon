import datetime

def difference_in_mintues(start_time, stop_time):
    # start = datetime.datetime(start_time)
    # stop = datetime.datetime(stop_time)
    diff = stop_time - start_time
    minutes = diff.seconds / 60
    
    return minutes

def convert_minutes_to_hours(mins):
    pass

def convert_cost(rate, hours):
    pass

today = datetime.datetime.now()

start_time = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
future_time = today + datetime.timedelta(hours=8)
# print(today)
# print(future_time)
end_time = datetime.datetime(today.year, today.month, today.day, future_time.hour, today.minute, today.second)

print(difference_in_mintues(start_time, end_time) / 60)