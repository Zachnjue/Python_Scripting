'''
fo = open('newdemo.txt', 'w')
fo.write('This is the first line\nThis is the second line\nThis is the third line')
# confirm what the mode is in
#print(fo.mode)
# result to false since the file is only writable
#print(fo.readable())
# result to true since the file is writable
#print(fo.writable())
fo.close()
'''
# Different Modes include: w - Write ,  r - Read, a - Append

'''
my_content = ['This is using loop-iteration-1', 'This is using loop-iteration-2', 'This is using loop-iteration-3']

fo = open('random.txt', 'a')

for each_line in my_content:
    fo.write(each_line + "\n")
    
fo.close()
'''

# Use of r Mode
fo = open('random.txt', 'r')
#data = fo.read()
# can use readline() - Read individual sentence from the file and readlines - read all lines in a file
data = fo.readlines()
fo.close()


print(data)