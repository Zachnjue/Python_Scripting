# The ones added on the command line wheb exectign a command.
import sys
# print(sys.argv[1])
#usr_str = input("Enter your string: ")
#user_action = input("Enter your action on your string(Valid actions are: lower/upper/title:  ")

if len(sys.argv) != 3:
    print("Usage: ")
    print(f'{sys.argv[0]} <your req string> <lower|lower|title>')
    sys.exit()

usr_str = sys.argv[1]
user_action = sys.argv[2]

if user_action == "lower":
    print(usr_str.lower())
elif user_action == "upper":
    print(usr_str.upper())
elif user_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid")
