first_month_sundays = 0
startday = 2
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_year = 1901
end_year = 2000
for year in range(start_year, end_year + 1):
    if year % 4 != 0:
        for j in days_in_months:
            startday += j
            if startday % 7 == 0:
                first_month_sundays += 1
    else:
        for j in leap_days_in_months:
            startday += j
            if startday % 7 == 0:
                first_month_sundays += 1
print(first_month_sundays)
