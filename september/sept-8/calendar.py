day_of_week = 3
month= "September"
year="2021"
month_year = month + " " + year
days_in_month=30

print(f"{month_year:^28}\n")
print("  S   M   T   W   T   F   S\n")

for spaces in range(day_of_week):
  print("    ", end="")

for day in range(1, days_in_month+1):
  print(f"{day:>3}", end=" ")
  day_of_week = day_of_week + 1
  if day_of_week == 7:
    print("\n")
    day_of_week = 0