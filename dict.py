my_dict = {'a': 1, 'b': 1, 'c': 3}

# prints only keys
for each in my_dict:
    print(each)

# prints both keys and values by using the .item() method
for key, value in my_dict.items():
    print(key, value)
