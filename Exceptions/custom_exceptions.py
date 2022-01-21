age = 23

# Use of raise
if age > 30:
    print("Valid age")
else:
    raise ValueError ("Age is less than 30")

# use of assert
age = 30

try:
    assert age<30
    print("Valid age")
except:
    print("Exceptin occured")