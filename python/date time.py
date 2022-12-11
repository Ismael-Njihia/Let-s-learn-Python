from datetime import datetime, timedelta

# Given date
given_date = datetime(2022, 7, 27)

# Calculate the duration of time (74 days and 5 hours)
duration = timedelta(days=74, hours=5)

# Calculate the previous date by subtracting the duration from the given date
previous_date = given_date - duration

# Display the previous date
print(previous_date.strftime("%d.%b.%y"))
