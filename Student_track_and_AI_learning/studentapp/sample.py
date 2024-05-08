import calendar

# Get the current year and month
current_year = 2023  # You can change this to any specific year
current_month = 11    # You can change this to any specific month (1 for January, 2 for February, ..., 12 for December)

# Get the list of all dates in the specified month
month_calendar = calendar.monthcalendar(current_year, current_month)

# Print all the dates in the month
for week in month_calendar:
    for day in week:
        if day != 0:
            print(f"{current_year}-{current_month:02d}-{day:02d}")
