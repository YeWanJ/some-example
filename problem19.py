days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 6
month = 1
year = 1901

sundays = 0
while year <= 2000:
    day += 7

    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        if day > days_of_month[month - 1] and month != 2:
            month += 1
            day -= days_of_month[month - 2]
        elif day > 29 and month == 2:
            month += 1
            day -= 29

    else:
        if day > days_of_month[month - 1]:
            month += 1
            day -= days_of_month[month - 2]

    if month > 12:
        year += 1
        month = 1

    if day == 1:
        sundays += 1


print(sundays)
