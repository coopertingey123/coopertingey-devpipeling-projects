year = int(input("Enter what year you want to know is a leap year: "))
if year >= 1000:
  if year % 400 == 0:
    print("true")
  elif year % 100 == 0:
    print("false")
  elif year % 4 == 0:
    print("true")
  else:
    print("false")
else:
  print("Years must be later than 1000")