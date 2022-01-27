import re
text = "This is a string this which is a THIS "
my_pat = r'this'
print(re.findall(my_pat, text, re.I))

text2 = """this is a string
This is a second line
this is third line
Yes, another one
"""
my_pat2 = r'^this'
print(re.findall(my_pat2, text2, re.M|re.I))   # re.M - it's a multiline 