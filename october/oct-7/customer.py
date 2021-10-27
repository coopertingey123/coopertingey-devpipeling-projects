import csv
# create a csv file of different customer orders where each row contains a customer order along with customer name address and phone number
# after you have built that out you will create a function to change the name, and for extra credit (because some customers change the phone numbers) add in a way to modify the phone number
# you are writing this from scratch so no outside libraries

def update_row():
    with open('customer_info.csv','r') as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        orders = list(csv_dict_reader)
        for order in orders:
            print(order)

    update_id = input('What entry do you want to change? ')
    field = input('What field do you want to change? ')
    
    for order in orders:
        if order['ID'] == update_id:
            new_value = input(f'Enter a new value for {field}: ')
            order[field] = new_value
            break

    with open('customer_info.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)

update_row()