# example of datetime module 1
'''
from datetime import date
today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# example 2
from datetime import date

my_date = date(2019, 11, 4)
print(my_date)

# creating a date object from a timestamp

A timestamp is simply a number representing the exact number of seconds that have passed since january 1, 1970(at 00:00:00 UTC)


from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

# Creating a date object using ISO Format

The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.


# The replace method()
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

# The Ctime function

The time module provides a function called Ctime, which converts the time in seconds since january 1, 1970(Unix epoch) to a string.

import time
timestamp = 1795514462.0117192
print(time.ctime(timestamp))


# The Calendar Module
import calendar
print(calendar.calendar(2000))


import calendar
calendar.prcal(2020)
'''

# Calendar for a specific month
import calendar
print(calendar.month(2020, 11))

# week header
import calendar
print(calendar.weekheader(2))

# leap year
import calendar
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))