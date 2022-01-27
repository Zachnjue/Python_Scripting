import re
text = "This is a pythonnn and python aaa haaafd aaaaa"

my_pat = r'\ba{3}\b'

print(re.findall(my_pat, text))