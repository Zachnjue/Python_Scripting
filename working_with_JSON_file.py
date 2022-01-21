import json

my_dict = {'Name':'Zach', 'skills':['Python', 'shell', 'yaml', 'AWS']}

req_file = "myjson.json" 

# Write a dictionary to the file
file_open = open(req_file, 'w')
json.dump(my_dict, file_open, indent=4)
file_open.close()

# read a json file
file_open = open(req_file, 'r')
print(json.load(file_open))
file_open.close()