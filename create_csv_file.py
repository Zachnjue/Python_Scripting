import csv

req_file = '/Users/zachnjue/Documents/Python /Scripting/CSV/writefile2.csv'

file_open = open(req_file, 'w', newline="") # newline helps to remove the blank spaces that appear on the csv file

csv_writer = csv.writer(file_open, delimiter=',')
'''
csv_writer.writerow(['First name', 'Second name', 'Age'])
csv_writer.writerow([1, 'Zachnjue', 30])
'''
my_data = [['First name', 'Second name', 'Age'], [1, 'Zachnjue', 30]]

csv_writer.writerows(my_data)
file_open.close()