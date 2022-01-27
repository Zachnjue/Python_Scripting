import re

text = "this python is for python2 and there two major vers python3 and python in future python4"
pat = r'\bpython[23]\b'
match_obj = re.search(pat,text)
# Matching the first index in a sentence
match_obj = re.match(pat,text, re.I)

if match_obj:
    print(match_obj)
    print("match from your pattern: ", match_obj.group())
    print("Starting index: ", match_obj.start())
    print('Ending index: ', match_obj.end())
    print("Length: ", match_obj.end() - match_obj.start())
else:
    print("No match found")
    
# re.match() - it matches the 0 index on the first line