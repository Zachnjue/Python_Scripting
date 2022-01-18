import csv
req_file = '/Users/zachnjue/Documents/Python /Scripting/CSV/info.csv'

file_open = open(req_file, 'r')
data = csv.reader(file_open, delimiter=',')    # use the Reader method to read the csv file. also important to use the delimiter option to separate the values
# Print the data as one list
print(list(data)[0])

# print data as each item of the list
for each in data:
    print(each)
file_open.close() 