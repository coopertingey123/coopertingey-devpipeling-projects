# import sqlite3

# connection = sqlite3.connect('dp_customers (5).db')
# cursor = connection.cursor()

# list_of_ids = [88, 89, 90]
# execute_line = "UPDATE Customers SET state = 'FL', postal_code = '34110' WHERE customer_id = ?"
# for num in list_of_ids:
#     execute_line = "UPDATE Customers SET state = 'FL', postal_code = '34110' WHERE customer_id = ?"
#     print(execute_line)
#     print(num)
#     cursor.execute(execute_line, (num,))

# connection.commit()


# print(rows)

# print(f"Name                      City             State  Postal Code")
# print('__________________________________________________________')
# for row in rows:
#     print(f'{row[0]:<25} {row[1]:<16} {row[2]:<6} {row[3]:<8}')


import sqlite3

connection = sqlite3.connect('dp_customers (5).db')
cursor = connection.cursor()

def view():
    customers = cursor.execute("SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers").fetchall()
    print(f'Customer ID    Name                       Address                         City                State          Zip            Phone          Email')

    for line in customers:
        print(f'{line[0]!s:<10}     {line[1]!s:<22}     {line[2]!s:<27}     {line[3]!s:<15}     {line[4]!s:<10}     {line[5]!s:<10}     {line[6]!s:<12}   {line[7]!s:<12}')
    return

def insert():
    view()
    name = input("Name:    ")
    address = input("Address: ")
    city = input("City:    ")
    state = input("State:  ")
    zipcode = input("Zipcode:  ")
    phone = input("Phone: ")
    email = input("Email:    ")
    list_of_values = name, address, city, state, zipcode, phone, email
    print(list_of_values)
    cursor.execute("INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", list_of_values)
    return

def update():
    view()
    customer_id = int(input("Which row would you like to update? (Select a customer id)\nEnter: "))
    field = input("Which field would you like to update? (name, street_address, city, state, postal_code, phone, email)\nEnter: ").lower()
    new_data = input("What is the new value you would like to update your data with?\nEnter here: ")
    list_of_values = new_data, customer_id
    print(list_of_values)
    cursor.execute("UPDATE Customers SET ({}) = ? WHERE customer_id = ?".format(field), list_of_values)
    return

def delete():
    view()
    customer_id = input("Which row would you like to delete? (Select a customer id) \nEnter here: ")
    cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id,))
    return

running = True

while running:
    selection = input("What would you like to do to the table? (R)ead, (D)elete, (U)pdate, (I)nsert, (E)xit \n Enter here: ").lower()
    if selection == 'd':
        delete()
    elif selection == 'u':
        update()
    elif selection == 'i':
        insert()
    elif selection == 'r':
        view()
    elif selection == 'e':
        running = False

connection.commit()
