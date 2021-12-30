import os
import sys
path = input("Enter your directory path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
    for each_file_dir in df_l:
        # print(each_file_dir)
        if os.path.isfile(each_file_dir):
            print(f"The {each_file_dir} is a file")
        else:
            print(f"The {each_file_dir} is a directory")
else:
    print("please provide valid path")
    sys.exit()
