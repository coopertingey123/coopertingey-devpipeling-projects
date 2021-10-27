import csv

with open('pgaTourData2.csv', 'r') as pgaTourData:
    list_of_data = csv.reader(pgaTourData)
    lists = []
    for line in list_of_data:
        lists.append(line)
    headers = lists[0]
    index_putts = int(headers.index('Average Putts'))
    bad_putters = []
    for item in lists[index_putts]:
        if item == float:
            if float(item[index_putts]) > 29.9:
                bad_putters.append(item[0])

    print(bad_putters)
        
