import os

path = input("Enter your path: ")

if os.path.exists(path):
    print(f"Given path: {path} is a valid path")
    if os.path.isfile(path):
        print("it is a file")
    else:
        print("it is a directory")
else:
    print(f"Given path: {path} is not existing on this host")
