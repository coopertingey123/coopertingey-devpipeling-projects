import csv

def print_menu():
   print('\n**** Address Book ****')
   print('What would you like to do?')
   print(' (A)dd a name')
   print(' (R)emove a name')
   print(' (F)ind a name')
   print(' (Q)uit')

def print_address_book(list_of_dicts, search='', with_indexes=False):
   leader_title = ''
   leader_lines = ''
   if with_indexes:
      leader_title = 'Index '
      leader_lines = '------'
   print(f'{leader_title} {"First Name":^10} {"Last Name":^15} {"Address":^20} {"City":^15} {"State":^6}')
   print(f'{leader_lines} {"-"*10} {"-"*15} {"-"*20} {"-"*15} {"-"*6}')
   
   for index, row in enumerate(list_of_dicts):
      num_string = ''
      if with_indexes:
         num_string = f'{index:6}. '
      
      matches_search = True
      if search:
         if not (search in row["First Name"] or \
         search in row["Last Name"] or \
             #Entered a space here in the last name thing
         search in row["Address"] or \
         search in row["City"] or \
         search in row["State"]):
            matches_search = False
      if matches_search:
         print(f'{num_string} {row["First Name"]:10} {row["Last Name"]:15} {row["Address"]:20} {row["City"]:15} {row["State"]:^6}')

def find_user():
   input_value = input('Enter a search term: ').lower()
   return input_value

def add_user(address_book):
   print('Add a new User:')
   new_user = {}
   new_user["First Name"] = input(' First Name: ')
   new_user["Last Name"] = input('  Last Name: ')
   new_user["Address"] = input('    Address: ')
   new_user["City"] = input('       City: ')
   new_user["State"] = input('      State: ')
   
   address_book.append(new_user)


def remove_user(address_book):
   print_address_book(address_book, with_indexes=True)
   user_input = int(input('Which user would you like to remove? (Enter number) '))
   address_book.pop(user_input)

def save_address_book(address_book):
   with open('address_book.csv', 'w', newline='') as csvout:
      csvwriter = csv.DictWriter(csvout, fieldnames=address_book[0].keys())
      csvwriter.writeheader()
      csvwriter.writerows(address_book)


def open_address_book():
   # Load the address book
   # Fields "First Name", "Last Name", "Address", "City", "State"]
   address_book = []

   search_term = ''

   # Moved this section of code from line 69 to here
   with open('address_book.csv', 'r', newline='') as csvfile:
      csvreader = csv.DictReader(csvfile)
      for row in csvreader:
         address_book.append(row)

   # Application Loop
   while True:
      print_address_book(address_book, search=search_term)
      search_term = ''
      print_menu()
      user_input = input()

      if user_input.upper() == 'A':
         add_user(address_book)                #added .upper() to all inputs
         print("New user added!\n")
         save_address_book(address_book)
      elif user_input.upper() == 'R':
         remove_user(address_book)
         print("User removed! \n")
         save_address_book(address_book)
      elif user_input.upper() == 'F':
         search_term = find_user()
      elif user_input.upper() == 'Q':
         break


   # Moved this section of code from line 69 to here
   # with open('address_book.csv', 'r', newline='') as csvfile:
   #    csvreader = csv.DictReader(csvfile)
   #    for row in csvreader:
   #       address_book.append(row)


   # Bugs
   # Search term. When I search "Cooper," it comes up with this:
   # Traceback (most recent call last):
   #   File "C:\Users\14802\Desktop\DevPipeline\sept-27\app.py", line 72, in <module>
   #     print_address_book(address_book, search=search_term)
   #   File "C:\Users\14802\Desktop\DevPipeline\sept-27\app.py", line 28, in print_address_book
   #     search in row["LastName"] or \
   # KeyError: 'LastName'