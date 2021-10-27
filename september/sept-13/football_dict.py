football_dict = {
  "ohio": "Buckeyes",
  "ASU": "Sun devils",
  "Utah": "Utes",
  "Clemson": "Tigers"
}
action = input("What would you like to do? \n (A)dd a team \n (R)emove a team \n (Q)uit \n input: ")

if action == "a":
  new_team = input('What is the university of the new team?')
  new_mascot = input('What is the mascot of the new team?')
  football_dict[new_team] = new_mascot

if action == "r":
  remove_team = input('What is the university of the new team?')
  # new_mascot = input('What is the mascot of the new team?')
  football_dict.remove(remove_team)

for teams in football_dict.items():
  team, mascot = teams
  print("{:<16} {:20}".format(team, mascot))