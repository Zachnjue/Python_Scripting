import re

my_str = "This is python and we are having python2 and python2 version"
my_pat = r'\bpython[23]?\b'

# finditer is for iterations
for each_obj in re.finditer(my_pat, my_str):
    print(f"The match is: {each_obj} and the starting index is {each_obj.start()}, ending index {each_obj.end()} ")