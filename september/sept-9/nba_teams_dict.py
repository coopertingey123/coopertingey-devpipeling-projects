# NBA TEAMS
teams = {
  "Phoenix": "Suns",
  "Dallas": "Mavericks",
  "Los Angeles": "Lakers"
}
print(teams)
prompt1 = input("What would you like to do? \n (Q)uit the program \n (A)dd a new team \n (R)emove a team \n")


# while prompt1 != "Q":
if prompt1 == "A":
  city = input("Enter the team's city: ")
  name = input("Enter the team's name: ")
  teams[f"{city}"] = name
elif prompt1 == "R":
  city = input("Enter the team's city: ")
  teams.remove([city])
  
print(teams)