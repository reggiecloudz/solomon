import datetime
from decimal import Decimal

def difference_in_mintues(start, stop):
    # convert the date strings in the the first item of the work_periods
    start_time = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    stop_time = datetime.datetime.strptime(stop, '%Y-%m-%d %H:%M:%S.%f')

    # get the difference between the time in minutes

    # first convert datetimes to a datetime objects
    start_date_time_obj = datetime.datetime(start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute, start_time.second)
    stop_date_time_obj = datetime.datetime(stop_time.year, stop_time.month, stop_time.day, stop_time.hour, stop_time.minute, stop_time.second)
    
    diff = stop_date_time_obj - start_date_time_obj
    minutes = diff.seconds / 60
    
    return minutes

def convert_minutes_to_hours(mins):
    return mins / 60

def convert_cost(rate, hours):
    return rate * Decimal.from_float(hours)

# test data
today = datetime.datetime.now()
future_time = today + datetime.timedelta(hours=8)
rate = Decimal(20.0)

# get list of work periods
work_periods = []

# when the job is started a new work period is created
work_period = {'start': today.__str__(), 'pause': '' }

# the new work_period is inserted into the work_periods list at the 0 index
work_periods.insert(0, work_period)

# when job is paused get the work_period at the 0 index and set the pause time
work_periods[0]["pause"] = future_time.__str__()

# get the minutes.
minutes = difference_in_mintues(work_periods[0]["start"], work_periods[0]["pause"])

# convert those minutes to hours
hours = convert_minutes_to_hours(minutes)

# get the cost of the job
cost = convert_cost(rate, hours)

# print(cost)