def leap_year(year):
  if year > 0:
    if year % 400 == 0:
      return "True"
    elif year % 100 == 0:
      return "False"
    elif year % 4 == 0:
      return "True"
    else:
      return "False"
  else:
    print("Years must be later than 0")

def day_of_the_week(year, month, day):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	year -= month < 3
	return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

def calendar(month, year):
    day_during_week = day_of_the_week(year, month, 1)
    if month == 1:
        month_year = "January" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 2:
        month_year = "February" + " " + str(year)
        print(f"{month_year:^28}\n")
        if leap_year(year) == True:
            days_in_month = 29
        else:
            days_in_month = 28
    elif month == 3:
        month_year = "March" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 4:
        month_year = "April" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 30
    elif month == 5:
        month_year = "May" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 6:
        month_year = "June" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 30
    elif month == 7:
        month_year = "July" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 8:
        month_year = "August" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 9:
        month_year = "September" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 30
    elif month == 10:
        month_year = "October" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31
    elif month == 11:
        month_year = "November" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 30
    elif month == 12:
        month_year = "December" + " " + str(year)
        print(f"{month_year:^28}\n")
        days_in_month = 31

    print("  S   M   T   W   T   F   S\n")

    for spaces in range(day_during_week):
        print("    ", end="")

    for day in range(1, days_in_month+1):
        print(f"{day:>3}", end=" ")
        day_during_week = day_during_week + 1
        if day_during_week == 7:
            print("\n")
            day_during_week = 0

month = int(input("Month for your calendar: "))
year = int(input("Year for your calendar (Any year after 1970): "))

calendar(month, year)

# print(day_of_the_week(year, month, 1))