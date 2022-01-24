import os
'''
req_path = input("Enter path to change working dir: ")
print("The current working dir is: ", os.getcwd())

try:
  os.chdir(req_path)
  print("Now your new working dir is: ", os.getcwd())
except FileNotFoundError:
  print('Given path is not a valid path . So cant change working directory')
except NotADirectoryError:
    print("Given a path is a file path. Can't change working directory")
except PermissionError:
    print("Sorry you don't have the necessary permissions to access the file")
except Exception as e:
    print(e)
'''
# For ease of importing the code as a module, always wrap in in a main function
def main():
    req_path = input("Enter path to change working dir: ")
    print("The current working dir is: ", os.getcwd())

    try:
        os.chdir(req_path)
        print("Now your new working dir is: ", os.getcwd())
    except FileNotFoundError:
        print('Given path is not a valid path . So cant change working directory')
    except NotADirectoryError:
        print("Given a path is a file path. Can't change working directory")
    except PermissionError:
        print("Sorry you don't have the necessary permissions to access the file")
    except Exception as e:
        print(e) 
if __name__ == '__main__':
    main()