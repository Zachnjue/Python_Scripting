import os
#import sys

req_path = input("Enter yout directory path: ")

if os.path.isfile(req_path):
    print(
        f"the given path {req_path} is a file. Please pass only directory path")
    # sys.exit()
else:
    all_files_dir = os.listdir(req_path)
    if len(all_files_dir) == 0:
        print(f"The given path is {req_path} an empty path")
    else:
        req_ex = input(
            'Enter the required files extensions .py/.sh/.log/.txt: ')
        req_files = []
        for each_f in all_files_dir:
            if each_f.endswith(req_ex):
                req_files.append(each_f)
        if len(req_files) == 0:
            print(
                f"These files with an extension of {req_ex} are 0 in this location {req_path}")
        else:
            print(
                f"The required files are {req_files} and total to {len(req_files)}")
