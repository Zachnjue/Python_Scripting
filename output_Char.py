import os

stringWord = input("Please enter your string: ")

sum = 0
for each in stringWord:
    print(f"{each} --> {sum}")
    sum += 1
