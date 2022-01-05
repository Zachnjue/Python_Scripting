import os
import sys
from datetime import datetime 

req_path = input("Enter your path: ")
age = 3

if not os.path.exists(req_path):
    sys.exit()
if os.path.isfile(req_path):
    sys.exit()

today_date = datetime.now()
#print(today_date)

for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_creation_date = datetime.fromtimestamp(os.path.getctime(each_file_path))
        no_of_days = today_date - file_creation_date
        #print(no_of_days)
        print(each_file_path, no_of_days)
        
        