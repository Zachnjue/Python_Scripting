import os

req_file = input("Enter your file name: "
for r, d, f in os.walk("/"):
    # r- root, d=directory and f=files
    for each_file in f:
        if each_file == req_file:
            print(os.path.join(r, each_file))
