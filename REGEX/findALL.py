import re

text = "This is python and it is easy to learn. This is my ip of a DB Servere: 255.100.102.103"

my_pattern = "i[st]"
my_pattern = "\w\w"
my_pattern="\d\d\d"

print(re.findall(my_pattern, text))
# Number of times my pattern reappears
print(len(re.findall(my_pattern, text)))
