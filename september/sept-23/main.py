import csv

# fields = ['FirstName', "LastName", "Title", "Birthdate"]

data = [{'FirstName': 'Jim', 'LastName': 'Halpert', 'Title': 'Sales Rep', 'Birthdate': '10/20/1979'},
{'FirstName': 'Michael', 'LastName': 'Scott', 'Title': 'Regional Manager', 'Birthdate': '08/16/1962'},
{'FirstName': 'Pam', 'LastName': 'Beesly', 'Title': 'Receptionist', 'Birthdate': '03/07/1974'},
{'FirstName': 'Dwight', 'LastName': 'Schrute', 'Title': 'Assistant to the Regional Manager', 'Birthdate': '01/20/1966'}]

fields = []
for key in data[0].keys():
  fields.append(key)

with open('office_employees.csv', 'w', newline='') as csvfile:
  csvwriter = csv.DictWriter(csvfile, fieldnames = fields)
  csvwriter.writeheader()
  csvwriter.writerows(data)